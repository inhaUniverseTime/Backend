import sqlite3

def convertToBinaryData(filename):
    # 디지털 데이터를 바이너리 포멧으로 변경
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB1th(location,result,image):
    try:
        sqliteConnection = sqlite3.connect(r'C:\Users\ins55\OneDrive\바탕 화면\database.db')
        cursor = sqliteConnection.cursor()
        print("SQLite 연결 완료")
        sqlite_insert_blob_query = """ INSERT INTO '30분~1시간 놀래' ('위치','결과값', '사진') VALUES (?, ?, ?)"""

        BLOB_image = convertToBinaryData(image)
        # 튜플 포멧으로 데이터 변환
        data_tuple = (location,result,BLOB_image)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("이미지 및 텍스트 DB 저장 완료")
        cursor.close()

    except sqlite3.Error as error:
        print("테이블 저장 실패", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite 연결 종료")

insertBLOB1th('학교','대운동장 축구',r'C:\Users\ins55\Downloads\대운동장.jpg')
insertBLOB1th('학교','대운동장 농구',r'C:\Users\ins55\Downloads\대운동장.jpg')
insertBLOB1th('학교','인경호',r'C:\Users\ins55\Downloads\인경호.jpg')
insertBLOB1th('학교','우남호',r'C:\Users\ins55\Downloads\우남호.jpg')
insertBLOB1th('학교','하이데거',r'C:\Users\ins55\Downloads\하이데거.jpg')












