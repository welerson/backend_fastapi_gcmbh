def gerar_relatorio_html(df):
    dias = df['Dia da Semana'].value_counts(normalize=True) * 100
    top_dias = dias.sort_values(ascending=False).head(3)

    linhas_html = ""
    for dia, prob in top_dias.items():
        linhas_html += f"""
        <tr>
            <td>{dia}</td>
            <td>{prob:.2f}%</td>
            <td>00:00 - 04:00</td>
            <td>Alta incidência histórica nesse horário.</td>
        </tr>"""

    html = f"""
    <div id="relatorio" style="font-family: Arial; padding: 20px;">
        <h2>Previsão de Arrombamentos - Av. Padre Pedro Pinto</h2>
        <p><strong>Gerado em:</strong> 11/05/2025</p>
        <table border="1" style="width:100%; border-collapse: collapse;">
            <tr><th>Dia</th><th>Probabilidade</th><th>Faixa Horária Crítica</th><th>Justificativa</th></tr>
            {linhas_html}
        </table>
    </div>
    """
    return html
