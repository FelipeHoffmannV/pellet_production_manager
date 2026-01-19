def processar_tempo_producao(form_instance):
    # Valores constantes
    PESO_POR_PACOTE = 1260
    CAPACIDADE_POR_MINUTO = 112.5
    TEMPO_BASE_TURNO = 460

    if form_instance:
        quantidade = form_instance.quantidadeProduzida 
        
        quantidade_em_kg = quantidade * PESO_POR_PACOTE
        calculo_de_tempo_trabalhado = quantidade_em_kg / CAPACIDADE_POR_MINUTO
        calculo_de_tempo_perdido = TEMPO_BASE_TURNO - calculo_de_tempo_trabalhado

        return {
            'tempo_perdido': calculo_de_tempo_perdido,
            'tempo_trabalhado': calculo_de_tempo_trabalhado
        }
