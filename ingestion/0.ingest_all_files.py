# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

dbutils.widgets.text("p_file_date", "2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")

# COMMAND ----------

#v_result = dbutils.notebook.run("1.ingest_circuits_file", 0, {"p_data_source": #"Ergast API", "p_file_date": "2021-04-18"})

v_result = dbutils.notebook.run("1.ingest_circuits_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})


# COMMAND ----------

v_result

# COMMAND ----------

#v_result = dbutils.notebook.run("2.ingest_races_file", 0, {"p_data_source": "Ergast #API", "p_file_date": "2021-04-18"})

v_result = dbutils.notebook.run("2.ingest_races_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})

# COMMAND ----------

v_result

# COMMAND ----------

#v_result = dbutils.notebook.run("3.ingest_constructors_file", 0, {"p_data_source": #"Ergast API", "p_file_date": "2021-04-18"})
v_result = dbutils.notebook.run("3.ingest_constructors_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})

# COMMAND ----------

v_result

# COMMAND ----------

#v_result = dbutils.notebook.run("4.ingest_drivers_file", 0, {"p_data_source": #"Ergast API", "p_file_date": "2021-04-18"})
v_result = dbutils.notebook.run("4.ingest_drivers_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})

# COMMAND ----------

v_result

# COMMAND ----------

#v_result = dbutils.notebook.run("5.ingest_results_file", 0, {"p_data_source": #"Ergast API", "p_file_date": "2021-04-18"})
v_result = dbutils.notebook.run("5.ingest_results_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})

# COMMAND ----------

v_result

# COMMAND ----------

#v_result = dbutils.notebook.run("6.ingest_pit_stops_file", 0, {"p_data_source": #"Ergast API", "p_file_date": "2021-04-18"})
v_result = dbutils.notebook.run("6.ingest_pit_stops_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})

# COMMAND ----------

v_result

# COMMAND ----------

#v_result = dbutils.notebook.run("7.ingest_lap_times_file", 0, {"p_data_source": #"Ergast API", "p_file_date": "2021-04-18"})
v_result = dbutils.notebook.run("7.ingest_lap_times_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})

# COMMAND ----------

v_result

# COMMAND ----------

#v_result = dbutils.notebook.run("8.ingest_qualifying_file", 0, {"p_data_source": #"Ergast API", "p_file_date": "2021-04-18"})
v_result = dbutils.notebook.run("8.ingest_qualifying_file", 0, {
    "p_data_source": v_data_source,
    "p_file_date": v_file_date
})

# COMMAND ----------

v_result

# COMMAND ----------


