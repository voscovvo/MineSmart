import sqlite3

import pygame.font

from commonFunctions import print_text
from commonSettings import *


def db_create():

    pass


def db_get_players_scores(level):
    """returns table: player_id, name, prev score, record score"""
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    sql = """
        SELECT p.player_id, p.player_name, rs.score, pls.record_score, MAX(rs.round_id) FROM player p
        LEFT JOIN player_level_scores pls ON p.player_id = pls.player_id AND pls.level_id = ?
        LEFT JOIN round_scores rs ON p.player_id = rs.player_id AND rs.level_id = ?
        GROUP BY p.player_name
        ORDER BY p.player_id ASC
    """.format(table='t')
    cursor.execute(sql, (level, level))
    db_result = cursor.fetchall()
    #print("DB RESULT: ",db_result)
    conn.close()
    return db_result

def db_get_player_name(id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    sql = "SELECT player_name FROM player WHERE player_id = ?"
    cursor.execute(sql, (id, ))
    db_result = cursor.fetchall()
    conn.close()
    return db_result[0][0]

def db_get_level_name(id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    sql = "SELECT level_name FROM game_levels WHERE gamelevel_id = ?"
    cursor.execute(sql, (id, ))
    db_result = cursor.fetchall()
    conn.close()
    return db_result[0][0]


def db_add_round_result(player, level, score):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    sql='INSERT INTO round_scores (player_id, level_id, score) VALUES('+str(player)+', '+str(level)+', '+str(score)+')'
    cursor.execute(sql)
    conn.commit()
    #db_result = cursor.fetchall()

    print("DB ROUND RESULT UPDATED: ", str(score))
    conn.close()


def db_update_new_record(player, level, score):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    sql = 'SELECT record_score FROM player_level_scores WHERE player_id = '+str(player)+' AND level_id = '+str(level)

    cursor.execute(sql)
    db_result = cursor.fetchall()
    #print("DB RESULT in RECORD CHECK: ", db_result)

    if db_result[0][0] < score:
        sql = 'UPDATE player_level_scores SET record_score='+str(score)+' WHERE player_id= '+str(player)+' AND level_id = '+str(level)
        cursor.execute(sql)
        conn.commit()
        print("DB RECORD UPDATED: ", str(score))
        #db_result = cursor.fetchall()
    print("DB RECORD NOT UPDATED: ", str(db_result[0][0]))
    conn.close()

    pass



# to Avoid Database errors
# try:
#     cursor.execute(sql_statement)
#     result = cursor.fetchall()
# except sqlite3.DatabaseError as err:
#     print("Error: ", err)
# else:
#     conn.commit()