from pyspark.sql import SparkSession

# 1️⃣ Cria a sessão Spark
spark = (
    SparkSession.builder
    .appName("IngestClientes")
    .master("local[*]")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3")
    .getOrCreate()
)

# 2️⃣ Configurações do banco PostgreSQL
DB_HOST = 'db'          # nome do container do banco (ver docker-compose)
DB_PORT = '5432'
DB_NAME = 'mydb'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'

url = f"jdbc:postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3️⃣ Lê a tabela de clientes
df_clientes = (
    spark.read.format("jdbc")
    .option("url", url)
    .option("dbtable", "db_loja.clientes")
    .option("user", DB_USER)
    .option("password", DB_PASSWORD)
    .option("driver", "org.postgresql.Driver")
    .load()
)

# 4️⃣ Exibe dados e estatísticas
df_clientes.show(5)
print(f"Total de clientes: {df_clientes.count()}")
