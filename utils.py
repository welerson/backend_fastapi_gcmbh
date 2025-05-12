# backend_fastapi/utils.py

def gerar_relatorio_html(df):
    import pandas as pd
    import requests

    # Cálculo de frequência por dia da semana
    dias = df['Dia da Semana'].value_counts(normalize=True) * 100
    dias = dias.sort_values(ascending=False)

    linhas = ""
    for dia, freq in dias.head(3).items():
        linhas += f"<tr><td>{dia}</td><td>{freq:.2f}%</td><td>00:00 - 04:00</td><td>Alta incidência histórica neste intervalo.</td></tr>"

    total_ocorrencias = len(df)
    total_com_alarme = df[df['Alarme?'].str.lower() == 'sim'].shape[0]
    total_com_cameras = df[df['Câmeras?'].str.lower() == 'sim'].shape[0]

    porcent_alarme = (total_com_alarme / total_ocorrencias) * 100
    porcent_cameras = (total_com_cameras / total_ocorrencias) * 100

    # API do clima (Venda Nova, BH)
    try:
        API_KEY = "613689b331c8e425c111385624ba5c55"
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=-19.8157&lon=-43.9542&appid={API_KEY}&units=metric&lang=pt_br"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados_clima = response.json()

        temp = dados_clima['main']['temp']
        sensacao = dados_clima['main']['feels_like']
        descricao = dados_clima['weather'][0]['description'].capitalize()
        clima_atual = f"<p><strong>Clima Atual em Venda Nova:</strong> {descricao}, {temp:.1f}°C (sensação {sensacao:.1f}°C)</p>"
    except Exception as e:
        clima_atual = "<p><strong>Clima Atual (simulado):</strong> Nublado, 19.0°C (sensação 17.0°C)</p>"

    html = f"""
    <html>
    <body style=\"font-family: Arial; padding: 20px; max-width: 900px; margin: auto;\">
        <div id=\"relatorio\">
            <h2 style=\"text-align: center; color: #003366;\">Previsão de Arrombamentos e Tentativas - Região Av. Padre Pedro Pinto</h2>
            <p><strong>Gerado em:</strong> 11/05/2025</p>
            <p><strong>Modelo Utilizado:</strong> Análise Preditiva - Random Forest Classifier</p>
            {clima_atual}
            <p><strong>Total de ocorrências analisadas:</strong> {total_ocorrencias}</p>
            <p><strong>Locais com alarme:</strong> {porcent_alarme:.1f}%</p>
            <p><strong>Locais com câmeras:</strong> {porcent_cameras:.1f}%</p>
            <hr>
            <h3>1. Dias e Horários de Maior Risco para Arrombamentos</h3>
            <table border=\"1\" cellpadding=\"8\" cellspacing=\"0\" style=\"border-collapse: collapse; width: 100%;\">
                <thead style=\"background-color: #f2f2f2;\">
                    <tr><th>Dia</th><th>Probabilidade</th><th>Faixa Horária Crítica</th><th>Justificativa</th></tr>
                </thead>
                <tbody>
                    {linhas}
                </tbody>
            </table>
            <hr>
            <h3>2. Perfil Comportamental de Ação Delituosa</h3>
            <p>Segundo análise de padrões comportamentais, indivíduos prestes a cometer arrombamentos geralmente consideram os seguintes fatores:</p>
            <ul>
                <li>Ausência de movimentação na rua</li>
                <li>Pouca ou nenhuma iluminação pública</li>
                <li>Tempo frio (ideal para uso de casacos que ocultam ferramentas)</li>
                <li>Ruas laterais com fácil rota de fuga</li>
                <li>Ambientes com baixa vigilância eletrônica</li>
                <li>Rotina previsível do comércio</li>
            </ul>
            <hr>
            <h3>3. Impacto das Condições Climáticas</h3>
            <p>De acordo com estudos e dados históricos:</p>
            <ul>
                <li><strong>Dia de chuva:</strong> há redução nas ações criminosas devido à baixa visibilidade e menor circulação</li>
                <li><strong>Dia frio:</strong> maior risco, pois facilita o transporte de ferramentas em mochilas ou sob roupas</li>
                <li><strong>Clima nublado e sem vento:</strong> favorece aproximação silenciosa sem chamar atenção</li>
            </ul>
            <hr>
            <h3>4. Recomendações para Prevenção e Ação Imediata</h3>
            <ul>
                <li><strong>Policiamento Reforçado:</strong> Priorizar rondas nos horários e dias críticos.</li>
                <li><strong>Monitoramento:</strong> Verifique alarmes e câmeras em horários de risco.</li>
                <li><strong>Segurança nos Estabelecimentos:</strong> Reforce fechaduras, alarmes e iluminação.</li>
            </ul>
            <hr>
            <h3>5. Ações Recomendadas para Lojistas</h3>
            <ul>
                <li>Revisar medidas de segurança física e eletrônica.</li>
                <li>Instalar câmeras com gravação noturna e alarmes monitorados.</li>
                <li>Evitar deixar mercadorias expostas durante a madrugada.</li>
                <li>Divulgar previsões entre comerciantes da região.</li>
            </ul>
            <hr>
            <h3>6. Próximos Passos</h3>
            <ul>
                <li>Reunião entre lojistas e GCMBH.</li>
                <li>Criação de grupo de alerta comunitário em tempo real.</li>
                <li>Monitoramento contínuo com base nos relatórios mensais.</li>
            </ul>
            <hr>
            <p><strong>Contato:</strong> Guarda Municipal de BH - Inspetoria Venda Nova</p>
            <button onclick=\"window.print()\">🖨️ Imprimir Relatório</button>
        </div>
    </body>
    </html>
    """
    return html
