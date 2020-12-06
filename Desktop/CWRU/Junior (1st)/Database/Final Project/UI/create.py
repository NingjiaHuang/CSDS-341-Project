import sqlite3
 
def create_tables():
    conn = sqlite3.connect('data.db')
    conn.text_factory = str
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS PATIENT
            ([pid] INTEGER PRIMARY KEY,
            [pname] TEXT NOT NULL,
            [pgender] TEXT NOT NULL,
            [p_bday] TEXT DEFAULT "N/A",
            [pphone] TEXT NOT NULL,
            [paddress] TEXT DEFAULT "N/A",
            [date_admitted] TEXT NOT NULL,
            [insurance_id] TEXT DEFAULT "N/A",
            [insurance_plan] TEXT DEFAULT "N/A"
            )''')

    c.execute("INSERT OR IGNORE INTO PATIENT VALUES (1, 'Kristin Manson', 'F', '1988-12-07', '216-556-7788', '3000  Lincoln Drive, Harrisburg, PA', '2020-06-09', 'ZGN001234', 'UnitedHealthcare')")
    c.execute("INSERT OR IGNORE INTO PATIENT VALUES (2, 'Michael R Beatty', 'M', '1989-09-09', '216-556-7788', '2204  Beechwood Avenue, HOOPER, UT', '2020-07-12', 'ZFT326890', 'UnitedHealthcare')")
    c.execute("INSERT OR IGNORE INTO PATIENT VALUES (3, 'Carl P Peltz', 'M', '1975-08-23', '216-556-7788', '3823  Windy Ridge Road, Fort Wayne, IN', '2020-03-18', 'FMD001738', 'Aetna')")
    c.execute("INSERT OR IGNORE INTO PATIENT VALUES (4, 'Karen E Bickford', 'F', '1967-11-17', '216-556-7788', '551  New York Avenue, Cleburne, TX', '2020-06-09', 'ZXM001234', 'UnitedHealthcare')")
    c.execute("INSERT OR IGNORE INTO PATIENT VALUES (5, 'Darius R Young', 'M', '1988-05-22', '216-556-7788', '320  Blue Spruce Lane, Little Orleans, MD', '2020-06-09', 'TXN001994', 'Cigna')")
    c.execute("INSERT OR IGNORE INTO PATIENT VALUES (6, 'Elmer V Mansour', 'M', '1956-07-25', '865-471-8029', '1774  Buena Vista Avenue, Springfield, OR', '2020-11-03', 'MFW0012574', 'Aetna')")
    c.execute("INSERT OR IGNORE INTO PATIENT VALUES (7, 'Michael C Epps', 'M', '1981-02-24', '914-347-8657', '4181  Pallet Street, Fairview Park, NY', '2020-04-17', 'XCF032699', 'Cigna')")

    c.execute('''CREATE TABLE IF NOT EXISTS DIAGNOSIS
            ([diag_id] TEXT PRIMARY KEY,
            [dname] TEXT NOT NULL,
            [diag_pid] INTEGER NOT NULL,
            [pathology] TEXT DEFAULT "N/A",
            [symptoms] TEXT DEFAULT "N/A",
            [treatment] TEXT DEFAULT "N/A",
            FOREIGN KEY(diag_pid) REFERENCES PATIENT(did)
            )''')
    c.execute("INSERT OR IGNORE INTO DIAGNOSIS VALUES (1,'Erin Anderson', 1, 'Ossification', 'Pain radiating in the arms', 'Prescription')")
    c.execute("INSERT OR IGNORE INTO DIAGNOSIS VALUES (2,'Erin Anderson', 2, 'Ossification', 'Sharp neck pain', 'Surgery')")
    c.execute("INSERT OR IGNORE INTO DIAGNOSIS VALUES (3, 'Erin Anderson', 3, 'Radiculopathy', 'Bowel dysfunction', 'Prescription')")
    c.execute("INSERT OR IGNORE INTO DIAGNOSIS VALUES (4, 'Jeremy Amps', 4, 'Sciatica', 'Sharp, radiating pain', 'Prescription')")
   
    c.execute('''CREATE TABLE IF NOT EXISTS PRESCRIPTION
            ([pre_id] TEXT PRIMARY KEY,
            [dname] TEXT NOT NULL,
            [pre_pid] INT NOT NULL,
            [pre_name] TEXT NOT NULL,
            [quantity] INT NOT NULL,
            [price] DECIMAL(10,2) NOT NULL,
            FOREIGN KEY(pre_pid) REFERENCES PATIENT(did))
            ''')
    c.execute("INSERT OR IGNORE INTO PRESCRIPTION VALUES (1, 'Mansour Afshani', 5, 'Phenytoin', 5, 16.87)")
    c.execute("INSERT OR IGNORE INTO PRESCRIPTION VALUES (2, 'Richard Aguilera', 4 ,'Neurontin', 3, 47.99)")

    conn.commit()

def main():
    create_tables()
    
    
if __name__ == '__main__':
    main()