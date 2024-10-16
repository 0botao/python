from xmind import core

# Criar um novo workbook do XMind
workbook = core.Workbook()
sheet = workbook.createSheet()
sheet.setTitle("Mapa Conceitual Web 3.0")

# Definir a raiz do mapa
root_topic = sheet.getRootTopic()
root_topic.setTitle("Web 3.0")

# Adicionar os tópicos principais
evolucao_topic = root_topic.addSubTopic()
evolucao_topic.setTitle("Evolução da Web")

caracteristicas_topic = root_topic.addSubTopic()
caracteristicas_topic.setTitle("Características")

funcionamento_topic = root_topic.addSubTopic()
funcionamento_topic.setTitle("Funcionamento")

beneficios_topic = root_topic.addSubTopic()
beneficios_topic.setTitle("Benefícios")

impactos_topic = root_topic.addSubTopic()
impactos_topic.setTitle("Impactos")

# Adicionar subtópicos para Evolução da Web
web1_topic = evolucao_topic.addSubTopic()
web1_topic.setTitle("Web 1.0")

web2_topic = evolucao_topic.addSubTopic()
web2_topic.setTitle("Web 2.0")

web3_topic = evolucao_topic.addSubTopic()
web3_topic.setTitle("Web 3.0")

# Adicionar subtópicos para Características
inteligencia_topic = caracteristicas_topic.addSubTopic()
inteligencia_topic.setTitle("Inteligência")

sociabilidade_topic = caracteristicas_topic.addSubTopic()
sociabilidade_topic.setTitle("Sociabilidade")

# ... (adicionar outras características)

# Adicionar subtópicos para Funcionamento
metadados_topic = funcionamento_topic.addSubTopic()
metadados_topic.setTitle("Metadados")

ontologias_topic = funcionamento_topic.addSubTopic()
ontologias_topic.setTitle("Ontologias")

# ... (adicionar outros elementos do funcionamento)

# Adicionar subtópicos para Benefícios
acesso_topic = beneficios_topic.addSubTopic()
acesso_topic.setTitle("Acesso à informação")

recursos_topic = beneficios_topic.addSubTopic()
recursos_topic.setTitle("Recursos avançados")

# ... (adicionar outros benefícios)

# Adicionar subtópicos para Impactos
positivos_topic = impactos_topic.addSubTopic()
positivos_topic.setTitle("Positivos")

negativos_topic = impactos_topic.addSubTopic()
negativos_topic.setTitle("Negativos")

# Salvar o workbook
workbook.save("mapa_conceitual_web3.xmind"),