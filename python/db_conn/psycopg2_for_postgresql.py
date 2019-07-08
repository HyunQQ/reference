# <Title>
# psycopg2를 통해 PostgreSQL에 접근 및 데이터 사용

# <Install>
# pip install psycopg2

# <Using Version>
# Python 3.6.5
# pip freeze | findstr psycopg2
# psycopg2==2.8.2
# psycopg2-binary==2.8.2

# <Reference>
# doc : http://initd.org/psycopg/docs/#
# tutorial : https://pynative.com/python-postgresql-tutorial/

# <Example Code>
import psycopg2

try:
    connection = psycopg2.connect(  user = "<데이터베이스 계정>",
                                    password = "<비밀번호>",
                                    host = "<호스트 주소>",
                                    port = "<사용 포트>",
                                    database = "<DB 이름>")
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(),"\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("connected to ",record,"\n")

except(Exception, psycopg2.Error) as error:
    print("Error occure \n",error)
finally:
    if(connection):
        # insert의 경우 connection.commit() 해야 db에 적용됨
        cursor.close()
        connection.close()
        print("over")