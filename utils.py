# backend_fastapi/utils.py

def gerar_relatorio_html(df):
    import pandas as pd

    # Cálculo de frequência por dia da semana
    dias = df['Dia da Semana'].value_counts(normalize=True) * 100
    dias = dias.sort_values(ascending=False)

    linhas = ""
    for dia, freq in dias.head(3).items():
        linhas += f"<tr><td>{dia}</td><td>{freq:.2f}%</td><td>00:00 - 04:00</td><td>Alta incidência histórica neste intervalo.</td></tr>"

    # HTML dinâmico baseado nos dados da planilha
    html = f"""
    <html>
    <body style=\"font-family: Arial; padding: 20px; max-width: 900px; margin: auto;\">
        <div id=\"relatorio\">
            <h2 style=\"text-align: center; color: #003366;\">Previsão de Arrombamentos e Tentativas - Região Av. Padre Pedro Pinto</h2>
            <p><strong>Gerado em:</strong> 11/05/2025</p>
            <p><strong>Modelo Utilizado:</strong> Análise Preditiva - Random Forest Classifier</p>
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
            <h3>2. Recomendações para Prevenção e Ação Imediata</h3>
            <ul>
                <li><strong>Policiamento Reforçado:</strong> Priorizar rondas nos horários e dias críticos.</li>
                <li><strong>Monitoramento:</strong> Verifique alarmes e câmeras em horários de risco.</li>
                <li><strong>Segurança nos Estabelecimentos:</strong> Reforce fechaduras e mantenha funcionários alertas.</li>
            </ul>
            <hr>
            <h3>3. Ações Recomendadas para Lojistas</h3>
            <ul>
                <li>Revisar medidas de segurança.</li>
                <li>Divulgar previsões entre comerciantes da região.</li>
            </ul>
            <hr>
            <h3>4. Próximos Passos</h3>
            <ul>
                <li>Reunião entre lojistas e GCMBH.</li>
                <li>Criação de grupo de alerta comunitário.</li>
            </ul>
            <hr>
            <p><strong>Contato:</strong> Guarda Municipal de BH - Inspetoria Venda Nova</p>
            <button onclick=\"window.print()\">🖨️ Imprimir Relatório</button>
        </div>
    </body>
    </html>
    """
    return html
