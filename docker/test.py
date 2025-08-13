
content = 1
useridx = 1

sql = """INSERT INTO reply (state, content, User_useridx)
VALUES (1, %s, %s)
;""".format(content, useridx)
print(sql)