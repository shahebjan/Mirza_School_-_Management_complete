# # <<<---------------------------------Importing all important modules and packages---------------------------------------->>>

import pymysql
from flask import Flask, render_template, request

# # <<<-----------------------------------Making Database Connection---------------------------------------->>>

try:
    conn = pymysql.connect(host='localhost', user='root', password='', database='school_management', port=3306)
    print("Database connected")

    # with conn.cursor() as cur:
    #     sql = '''
    #     CREATE TABLE IF NOT EXISTS first_qrt_exam (
    #     class_name VARCHAR(50),
    #     student_id VARCHAR(50) UNIQUE,
    #     first_name VARCHAR(50) NOT NULL,
    #     last_name VARCHAR(50) NOT NULL,
    #     hindi_gain FLOAT,
    #     english_gain FLOAT,
    #     maths_gain FLOAT,
    #     science_gain FLOAT,
    #     computer_gain FLOAT,
    #     grand_total_gain FLOAT,
    #     percentage FLOAT,
    #     division VARCHAR(20),
    #     PRIMARY KEY (student_id)
    #     )
    #     '''
    #     cur.execute(sql)
    #     conn.commit()
    #     print("Table created")
    #     cur.close()
    #     conn.close()

    # with conn.cursor() as cur:
    #     sql = '''
    #     CREATE TABLE IF NOT EXISTS half_year_exam (
    #     class_name VARCHAR(50),
    #     student_id VARCHAR(50) UNIQUE,
    #     first_name VARCHAR(50) NOT NULL,
    #     last_name VARCHAR(50) NOT NULL,
    #     hindi_gain FLOAT,
    #     english_gain FLOAT,
    #     maths_gain FLOAT,
    #     science_gain FLOAT,
    #     computer_gain FLOAT,
    #     grand_total_gain FLOAT,
    #     percentage FLOAT,
    #     division VARCHAR(20),
    #     PRIMARY KEY (student_id)
    #     )
    #     '''
    #     cur.execute(sql)
    #     conn.commit()
    #     print("Table created")
    #     cur.close()
    #     conn.close()


    # with conn.cursor() as cur:
    #     sql = '''
    #     CREATE TABLE IF NOT EXISTS second_qrt_exam (
    #     class_name VARCHAR(50),
    #     student_id VARCHAR(50) UNIQUE,
    #     first_name VARCHAR(50) NOT NULL,
    #     last_name VARCHAR(50) NOT NULL,
    #     hindi_gain FLOAT,
    #     english_gain FLOAT,
    #     maths_gain FLOAT,
    #     science_gain FLOAT,
    #     computer_gain FLOAT,
    #     grand_total_gain FLOAT,
    #     percentage FLOAT,
    #     division VARCHAR(20),
    #     PRIMARY KEY (student_id)
    #     )
    #     '''
    #     cur.execute(sql)
    #     conn.commit()
    #     print("Table created")
    #     cur.close()
    #     conn.close()

    # with conn.cursor() as cur:
    #     sql = '''
    #     CREATE TABLE IF NOT EXISTS final_year_exam (
    #     class_name VARCHAR(50),
    #     student_id VARCHAR(50) UNIQUE,
    #     first_name VARCHAR(50) NOT NULL,
    #     last_name VARCHAR(50) NOT NULL,
    #     hindi_gain FLOAT,
    #     english_gain FLOAT,
    #     maths_gain FLOAT,
    #     science_gain FLOAT,
    #     computer_gain FLOAT,
    #     grand_total_gain FLOAT,
    #     percentage FLOAT,
    #     division VARCHAR(20),
    #     PRIMARY KEY (student_id)
    #     )
    #     '''
    #     cur.execute(sql)
    #     conn.commit()
    #     print("Table created")
    #     cur.close()
    #     conn.close()


# #<<<-------------------------------------------Making object of Flask-------------------------------------------->>>

    app = Flask(__name__)

# # <<<---------------------------- This route will open Mirza School & Management Website----------------------------------->>

    @app.route('/')
    def mirza_school():
        return render_template('/home.html')
    
# # <<<--------------------------------------This route will open About section---------------------------------------->>>

    @app.route('/about')
    def aboutme():
        return render_template('/aboutus.html')
    
# # <<<-----------------------------------This route will open Contact Us section---------------------------------->>>

    @app.route('/contactus')
    def contactus():
        return render_template('/contactus.html')
    
# # <<<--------------------------------This route will open Frst quartely exam form----------------------------------------->>>

    @app.route('/firstQrtExam')
    def firstQrtExam():
        return render_template('/first_quart_examination.html')

#<<<-------------------------------this route will take data input from first_qrt_exam_form------------------------->>>
 
    @app.route('/submit-first-qrt-exam', methods=['POST'])
    def submit_first_qrt_exam():
        with conn.cursor() as cur:
            if request.method=='POST':
                class_selected = request.form['Class']
                student_id = request.form['student_id']
                fname = request.form['first_name']
                lname = request.form['last_name']
                hindi_gain = float(request.form.get('hindi_gain', 0))
                english_gain = float(request.form.get('english_gain', 0))
                maths_gain = float(request.form.get('maths_gain', 0))
                science_gain = float(request.form.get('science_gain', 0))
                computer_gain = float(request.form.get('computer_gain', 0))
                grand_total_gain = hindi_gain + english_gain + maths_gain + science_gain + computer_gain
                percentage = (grand_total_gain / 500) * 100

#<<<-------------------------- Calculate division based on percentage------------------------------------>>>

                if percentage >= 80:
                    division = 'Distinction'
                elif percentage >= 60:
                    division = 'First'
                elif percentage >= 45:
                    division = 'Second'
                elif percentage >= 33:
                    division = 'Third'
                else:
                    division = 'Fail'

#<<<--------------------------------- Insert data into first_qrt_exam database------------------------------------------>>>

                sql = """
                INSERT INTO first_qrt_exam (class_name, student_id, first_name, last_name, hindi_gain, english_gain, maths_gain, science_gain,
                computer_gain, grand_total_gain, percentage, division)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                values = (class_selected, student_id, fname, lname, hindi_gain, english_gain, maths_gain, science_gain,
                        computer_gain, grand_total_gain, percentage, division)

                cur.execute(sql, values)
                conn.commit()

# # <<<------------------------------------Fetching all data in a table of first qrt exam to see---------------------------------------->>>
                
                query = 'select * from first_qrt_exam'
                cur.execute(query)
                data = cur.fetchall()
                return render_template('/first_qrt_exam_database.html', data=data)
    
# # <<<--------------------------------This route will open Half yearly exam form----------------------------------------->>>

    @app.route('/halfyearExam')
    def halfyearExam():
        return render_template('/half_year_examination.html')
    
# <<<----------------------This route will take input from user from half_year_exam_form----------------------------->>>

    @app.route('/submit-half-year-exam', methods=['POST'])
    def submit_half_year_exam():
        with conn.cursor() as cur:
            if request.method=='POST':
                class_selected = request.form['Class']
                student_id = request.form['student_id']
                fname = request.form['first_name']
                lname = request.form['last_name']
                hindi_gain = float(request.form.get('hindi_gain', 0))
                english_gain = float(request.form.get('english_gain', 0))
                maths_gain = float(request.form.get('maths_gain', 0))
                science_gain = float(request.form.get('science_gain', 0))
                computer_gain = float(request.form.get('computer_gain', 0))
                grand_total_gain = hindi_gain + english_gain + maths_gain + science_gain + computer_gain
                percentage = (grand_total_gain / 500) * 100

#<<<------------------------------ Calculate division based on percentage ---------------------------------->>>

                if percentage >= 80:
                    division = 'Distinction'
                elif percentage >= 60:
                    division = 'First'
                elif percentage >= 45:
                    division = 'Second'
                elif percentage >= 33:
                    division = 'Third'
                else:
                    division = 'Fail'

#<<<-------------------------------- Insert data into half_year_exam database -------------------------------------->>>

                sql = """
                INSERT INTO half_year_exam (class_name, student_id, first_name, last_name, hindi_gain, english_gain, maths_gain, science_gain,
                computer_gain, grand_total_gain, percentage, division)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                values = (class_selected, student_id, fname, lname, hindi_gain, english_gain, maths_gain, science_gain,
                        computer_gain, grand_total_gain, percentage, division)

                cur.execute(sql, values)
                conn.commit()

# # <<<-----------------------Fetching all data in a table of Half yearly exam to see-------------------------------->>>
                
                query = 'select * from half_year_exam'
                cur.execute(query)
                data = cur.fetchall()
                return render_template('/half_year_exam_database.html', data=data)
    
# # <<<--------------------------------This route will open Second quartely exam form-------------------------------------->>>

    @app.route('/secondQrtExam')
    def secondQrtExam():
        return render_template('/second_quart_examination.html')

#<<<-----------------------------This route will take input from user from second_qrt_exam_form------------------------------>>>
  
    @app.route('/submit-second-qrt-exam', methods=['POST'])
    def submit_second_qrt_exam():
        with conn.cursor() as cur:
            if request.method=='POST':
                class_selected = request.form['Class']
                student_id = request.form['student_id']
                fname = request.form['first_name']
                lname = request.form['last_name']
                hindi_gain = float(request.form.get('hindi_gain', 0))
                english_gain = float(request.form.get('english_gain', 0))
                maths_gain = float(request.form.get('maths_gain', 0))
                science_gain = float(request.form.get('science_gain', 0))
                computer_gain = float(request.form.get('computer_gain', 0))
                grand_total_gain = hindi_gain + english_gain + maths_gain + science_gain + computer_gain
                percentage = (grand_total_gain / 500) * 100

#<<<---------------------------------- Calculate division based on percentage---------------------------------------->>>

                if percentage >= 80:
                    division = 'Distinction'
                elif percentage >= 60:
                    division = 'First'
                elif percentage >= 45:
                    division = 'Second'
                elif percentage >= 33:
                    division = 'Third'
                else:
                    division = 'Fail'

#<<<---------------------------------- Insert data into second_qrt_exam database-------------------------------------->>>
                sql = """
                INSERT INTO second_qrt_exam (class_name, student_id, first_name, last_name, hindi_gain, english_gain, maths_gain, science_gain,
                computer_gain, grand_total_gain, percentage, division)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                values = (class_selected, student_id, fname, lname, hindi_gain, english_gain, maths_gain, science_gain,
                        computer_gain, grand_total_gain, percentage, division)

                cur.execute(sql, values)
                conn.commit()

# # <<<----------------------------------Fetching all data in a table of Second quarterly to see------------------------------------------->>>
                
                query = 'select * from second_qrt_exam'
                cur.execute(query)
                data = cur.fetchall()
                return render_template('/second_qrt_exam_database.html', data=data)

        
# # <<<--------------------------------This route will open Fianl yearly exam form----------------------------------------->>>

    @app.route('/finalyearExam')
    def finalyearExam():
        return render_template('/final_year_examination.html')
    
# <<<----------------------This route will take input from user from final_year_exam_form----------------------------->>>

    @app.route('/submit-final-year-exam', methods=['POST'])
    def submit_final_year_exam():
        with conn.cursor() as cur:
            if request.method=='POST':
                class_selected = request.form['Class']
                student_id = request.form['student_id']
                fname = request.form['first_name']
                lname = request.form['last_name']
                hindi_gain = float(request.form.get('hindi_gain', 0))
                english_gain = float(request.form.get('english_gain', 0))
                maths_gain = float(request.form.get('maths_gain', 0))
                science_gain = float(request.form.get('science_gain', 0))
                computer_gain = float(request.form.get('computer_gain', 0))
                grand_total_gain = hindi_gain + english_gain + maths_gain + science_gain + computer_gain
                percentage = (grand_total_gain / 500) * 100

#<<<------------------------------ Calculate division based on percentage ---------------------------------->>>

                if percentage >= 80:
                    division = 'Distinction'
                elif percentage >= 60:
                    division = 'First'
                elif percentage >= 45:
                    division = 'Second'
                elif percentage >= 33:
                    division = 'Third'
                else:
                    division = 'Fail'

#<<<-------------------------------- Insert data into final_year_exam database -------------------------------------->>>

                sql = """
                INSERT INTO final_year_exam (class_name, student_id, first_name, last_name, hindi_gain, english_gain, maths_gain, science_gain,
                computer_gain, grand_total_gain, percentage, division)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                values = (class_selected, student_id, fname, lname, hindi_gain, english_gain, maths_gain, science_gain,
                        computer_gain, grand_total_gain, percentage, division)

                cur.execute(sql, values)
                conn.commit()

# # <<<-----------------------Fetching all data in a table of Final yearly exam to see-------------------------------->>>
                
                query = 'select * from final_year_exam'
                cur.execute(query)
                data = cur.fetchall()
                return render_template('/final_year_exam_database.html', data=data)
    
 # <<<--------------------------------This route will open First quarter exam result form----------------------------------------->>>

    @app.route('/firstquartexamresult')
    def firstquartexamresult():
        return render_template('/first_quart_result.html')
    
# <<<---------------------This route will take inputs from user from first_qrt_exam_result-------------------------->>>

    @app.route('/frst-qrt-exm-rslt', methods=['POST'])
    def frst_qrt_exm_rslt():
        if request.method=='POST':
            student_id = request.form.get('student_id')
            with conn.cursor() as cur:
                sql = 'SELECT * FROM first_qrt_exam WHERE student_id = %s'
                cur.execute(sql, (student_id,))
                data = cur.fetchall()
                return render_template('first_qrt_result_database.html', data=data)

    
# # <<<--------------------------------This route will open Half yearly exam result form-------------------------------------->>>

    @app.route('/halfyearexamresult')
    def halfyearexamresult():
        return render_template('/half_year_result.html')
    
# <<<---------------------This route will take inputs from user from half_year_exam_result-------------------------->>>

    @app.route('/hlf-yr-exm-rslt', methods=['POST'])
    def half_yr_exm_rslt():
        if request.method=='POST':
            student_id = request.form.get('student_id')
            with conn.cursor() as cur:
                sql = 'SELECT * FROM half_year_exam WHERE student_id = %s'
                cur.execute(sql, (student_id,))
                data = cur.fetchall()
                return render_template('half_year_result_database.html', data=data)
    
# # <<<--------------------------------This route will open Second quarter exam result form----------------------------------------->>>

    @app.route('/secondquartexamresult')
    def secondquartexamresult():
        return render_template('/second_quart_result.html')
    

# <<<---------------------This route will take inputs from user from second_qrt_exam_result-------------------------->>>

    @app.route('/second-qrt-exm-rslt', methods=['POST'])
    def second_qrt_exm_rslt():
        if request.method=='POST':
            student_id = request.form.get('student_id')
            with conn.cursor() as cur:
                sql = 'SELECT * FROM second_qrt_exam WHERE student_id = %s'
                cur.execute(sql, (student_id,))
                data = cur.fetchall()
                return render_template('second_qrt_rslt_database.html', data=data)

# # <<<--------------------------------This route will open Final Year exam result form-------------------------------------->>>

    @app.route('/finalyearexamresult')
    def finalyearexamresult():
        return render_template('/final_year_result.html')
    
# <<<---------------------This route will take inputs from user from second_qrt_exam_result-------------------------->>>

    @app.route('/final-yr-exm-rslt', methods=['POST'])
    def final_yr_exm_rslt():
        if request.method=='POST':
            student_id = request.form.get('student_id')
            with conn.cursor() as cur:
                sql = 'SELECT * FROM final_year_exam WHERE student_id = %s'
                cur.execute(sql, (student_id,))
                data = cur.fetchall()
                return render_template('final_yr_rslt_database.html', data=data)

    
# # <<<-----------------------------This route will open Admission form to take inputs------------------------------------->>>

    @app.route('/admission')
    def admission_form():
        return render_template('/addmission_form.html')

# #<<<----------------------------------This route will get data after clicking submit-------------------------------------->>>

    @app.route('/submit', methods=['POST'])
    def submit():
        with conn.cursor() as cur:
            if request.method == 'POST':
                class_selected = request.form['Class']
                id = request.form['id']
                student_id = request.form['student_id']
                fname = request.form['fname']
                lname = request.form['lname']
                faname = request.form['faname']
                moname = request.form['moname']
                mobile_number = request.form['mobile_number']
                adharcard_number = request.form['adharcard_number']
                address = request.form['address']

# # # # # # <<<-----------------------------------Inserting all data into my selected table----------------------------------------------->>>

                sql = "INSERT INTO {} (id, student_id, first_name, last_name, father_name, mother_name, mobile_number, adhar_card, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)".format(class_selected)

                cur.execute(sql, (id, student_id, fname, lname, faname, moname, mobile_number, adharcard_number, address))
                conn.commit()

# # # # # # # # # <<<------------------------------------Fetching all data in a table to see----------------------------------------------->>>

                query = 'SELECT * FROM {}'.format(class_selected)
                cur.execute(query)
                data = cur.fetchall()
                return render_template('table.html', data=data)

# # # # # # # # #<<<------------------------------This route will open HTML Fees Submission Form to take inputs------------------------------->>>

    @app.route('/fees')
    def fees_form():
        return render_template('/fees_submission.html')

# # <<<-------------------------------------This route will get data after clicking submit------------------------------------------->>>

    @app.route('/submit-fees', methods=['POST'])
    def fees_submit():
        with conn.cursor() as cur:
            if request.method == 'POST':
                class_name = request.form['Class']
                id = request.form['id']
                student_id = request.form['student_id']
                first_name = request.form['fname']
                last_name = request.form['lname']
                april2023 = request.form['april2023']
                may2023 = request.form['may2023']
                june2023 = request.form['june2023']
                july2023 = request.form['july2023']
                august2023 = request.form['august2023']
                september2023 = request.form['september2023']
                october2023 = request.form['october2023']
                november2023 = request.form['november2023']
                december2023 = request.form['december2023']
                january2024 = request.form['january2024']
                february2024 = request.form['february2024']
                march2024 = request.form['march2024']

# #  <<<----------------------------------------Inserting all data into my fees_table----------------------------------------------->>>

                sql = "INSERT INTO fees_table (class_name, id, student_id, first_name, last_name, april2023, may2023, june2023, july2023, august2023, september2023, october2023, november2023, december2023, january2024, february2024, march2024) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (class_name, id, student_id, first_name, last_name, april2023, may2023, june2023, july2023, august2023, september2023, october2023, november2023, december2023, january2024, february2024, march2024)
                cur.execute(sql, values)
                conn.commit()

# # <<<------------------------------------Fetching all data in a table to see----------------------------------------------->>>
                
                query = 'select * from fees_table'
                cur.execute(query)
                data = cur.fetchall()
                return render_template('fees_database.html', data=data)
            


    if __name__ == '__main__':
        app.run(debug=True)

# # # <<<----------------------------------Handeling all errors & exceptions---------------------------------------------->>>

except Exception as e:
    print(e)


