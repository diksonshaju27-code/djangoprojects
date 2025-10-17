# nobel_prize
#
# year   subject  winner   country category
#
# 1970 Physics  hannes  sweden  scientist
#
# ---
#
#
# 1).write a sql query to find the nobel prize winners for the year 1970(return year,subject and winner)

# select * from nobel_prize where year=1970;
#
#
# # 2).write a sql query to find the nobel prize winnerin literature for 1971
#
# select * from nobel_prize where year=1971 and subject='literature';
# #nobel_prize
# # 3).sql to find the winners in the field of physics since 1978(return winner)
# #
# select * from nobel_prize where subject=physics and year>=1978;
#
# # 4)sql query to find the winners in chemistry between 1970 and 1980
#
# select * from  where subject=chemistry and year between 1970 and 1980;
#
# #
# # 5)sql query to find the details of the winners whose firstname match with string 'Louis'
#
# SELECT *from nobel_prize where winner LIKE 'Louis%';
#
# # 6).sql query to find the winners excluding subjects physiology and Economics.
# SELECT winner from nobel_prize where subject NOT IN ('Physiology', 'Economics');