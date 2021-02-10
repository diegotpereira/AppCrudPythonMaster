import sqlite3

conn = sqlite3.connect("db_tarefa.db")

def criar_tabela_todo():
    
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists tarefa (cd_tarefa integer primary key autoincrement, tarefa text, concluido integer)""")

def add_tarefa(tarefa):
    
    conn.execute("insert into tarefa (tarefa, concluido) values (?, 0)", (tarefa, ))
    conn.commit()

def remover_tarefa(cd_tarefa):
    
    conn.execute("delete from tarefa where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def concluir_tarefa(cd_tarefa):
    
    conn.execute("update tarefa set concluido = 1 where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def get_tarefas():
    
    return conn.execute("select cd_tarefa, tarefa, concluido from tarefa")