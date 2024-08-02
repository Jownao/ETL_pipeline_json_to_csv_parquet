from etl import pipeline_calculo_final

pasta_argumento = 'data'
formato_saida = ["csv","parquet"]

pipeline_calculo_final(pasta_argumento,formato_saida)