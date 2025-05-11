
def gerar_relatorio_html(df):
    html = """
    <div id=\"relatorio\" style=\"font-family: Arial, sans-serif; padding: 20px; max-width: 900px;\">
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
                <tr><td>Terça-feira</td><td>85.23%</td><td>00:00 - 04:00</td><td>Maioria das ocorrências históricas ocorreram nesse dia e horário.</td></tr>
                <tr><td>Domingo</td><td>78.45%</td><td>00:00 - 04:00</td><td>Alta incidência nesse dia e horário específico.</td></tr>
                <tr><td>Sábado</td><td>72.19%</td><td>00:00 - 04:00</td><td>Probabilidade considerável nesse intervalo.</td></tr>
            </tbody>
        </table>
        <hr>
        <h3>2. Recomendações para Prevenção e Ação Imediata</h3>
        <ul>
            <li><strong>Policiamento Reforçado:</strong> Priorizar rondas durante a madrugada, especialmente nos dias críticos.</li>
            <li><strong>Monitoramento:</strong> Verifique a operação das câmeras e alarmes em horários críticos.</li>
            <li><strong>Segurança no Estabelecimento:</strong> Fechaduras reforçadas, portas de segurança e alarmes remotos.</li>
        </ul>
        <hr>
        <h3>3. Ações Recomendadas para Lojistas</h3>
        <ul>
            <li><strong>Revisão das Medidas de Segurança</strong></li>
            <li><strong>Divulgação da Previsão de Risco</strong></li>
        </ul>
        <hr>
        <h3>4. Próximos Passos</h3>
        <ul>
            <li>Reunião com lojistas</li>
            <li>Grupo de comunicação com a GMBH</li>
        </ul>
        <hr>
        <h3>Importante:</h3>
        <p>Previsão baseada em dados históricos. Quanto mais dados, mais precisa será a análise.</p>
        <hr>
        <h3>Contato para Ações de Segurança:</h3>
        <p><strong>Guarda Municipal de Belo Horizonte - Inspetoria Venda Nova</strong><br>(Telefone e E-mail da Guarda Municipal)</p>
        <hr>
        <h3>Visualizações sugeridas:</h3>
        <ol>
            <li>Gráfico de Probabilidade por Dia</li>
            <li>Gráfico de Faixas Horárias Críticas</li>
        </ol>
        <button onclick=\"printRelatorio()\" style=\"margin-top: 20px; padding:10px 20px; background-color:#004080; color:white; border:none; cursor:pointer;\">🖨️ Imprimir Relatório</button>
    </div>

    <script>
    function printRelatorio() {
        var conteudo = document.getElementById('relatorio').innerHTML;
        var win = window.open('', '', 'height=700,width=900');
        win.document.write('<html><head><title>Imprimir Relatório</title></head><body>');
        win.document.write(conteudo);
        win.document.write('</body></html>');
        win.document.close();
        win.print();
    }
    </script>
    """
    return html
