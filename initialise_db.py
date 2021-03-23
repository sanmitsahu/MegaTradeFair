import mysql.connector as mysql
import db_conn

def initialise_db():
	initialise_country = """
			CREATE TABLE IF NOT EXISTS country (
			country_id int unique auto_increment not null,
			countryname varchar(255),
			PRIMARY KEY  (country_id)
			);
		"""
	initialise_state ="""
			CREATE TABLE IF NOT EXISTS state (
        	state_id int unique auto_increment not null,
        	statename varchar(255),
        	countryid int,
        	PRIMARY KEY  (state_id),
        	FOREIGN KEY (countryid) REFERENCES country (country_id) ON DELETE CASCADE
    		);
		"""
	initialise_industry = """
			CREATE TABLE IF NOT EXISTS industry (
		    industry_id int unique auto_increment not null,
		    industryname varchar(255),
		    PRIMARY KEY  (industry_id)
		    );
		"""

	initialise_venue = """
			CREATE TABLE IF NOT EXISTS venue (
	        venue_id int unique auto_increment not null,
	        cityname varchar(255),
	        address varchar(255),
	        countryid int,
	        stateid int,
	        PRIMARY KEY  (venue_id),
	        FOREIGN KEY (stateid) REFERENCES state (state_id) ON DELETE CASCADE,
	        FOREIGN KEY (countryid) REFERENCES country (country_id) ON DELETE CASCADE
    		);
		"""

	initialise_fair_event = """
	    	CREATE TABLE IF NOT EXISTS fair_event (
	        event_id int unique auto_increment not null,
	        event_name varchar(255),
	        bookingstartdate date not null,
	        startdate date not null,
	        enddate date not null,
	        venueid int,
	        PRIMARY KEY  (event_id),
	        FOREIGN KEY (venueid) REFERENCES venue (venue_id) ON DELETE CASCADE
	    	);
		"""

	initialise_stall = """
	    	CREATE TABLE IF NOT EXISTS stall (
	        stall_id int unique auto_increment not null,
	        stallno int not null,
	        price float not null,
	        stallsize int,
	        isbooked bit not null,
	        eventid int,
	        PRIMARY KEY  (stall_id),
	        FOREIGN KEY (eventid) REFERENCES fair_event (event_id) ON DELETE CASCADE
	    	);
		"""

	initialise_visitor = """
	   		CREATE TABLE IF NOT EXISTS visitor (
	        visitor_id int unique auto_increment not null,
	        firstname varchar(255),
	        lastname varchar(255),
	        address varchar(255),
	        pincode int not null,
	        mobileno varchar(255) not null,
	        email_id varchar(255) not null,
	        dateofbirth date,
	        gender bit not null,
	        PRIMARY KEY  (visitor_id)
	    	);
		"""

	initialise_exhibitor = """
	    	CREATE TABLE IF NOT EXISTS exhibitor (
	        exhibitor_id int unique auto_increment not null,
	        exhibitorname varchar(255),
	        email_id varchar(255),
	        phoneno varchar(255),
	        companyname varchar(255),
	        companydescription varchar(255),    
	        address varchar(255),
	        pincode int not null,
	        industryid int ,
	        countryid int ,
	        stateid int ,
	        PRIMARY KEY  (exhibitor_id),
	        FOREIGN KEY (industryid) REFERENCES industry (industry_id) ON DELETE CASCADE,
	        FOREIGN KEY (stateid) REFERENCES state (state_id) ON DELETE CASCADE,
	        FOREIGN KEY (countryid) REFERENCES country (country_id) ON DELETE CASCADE
	    	);
		"""

	initialise_booking = """
	    	CREATE TABLE IF NOT EXISTS booking (
	        booking_id int unique auto_increment not null,
	        bookingdate date not null,
	        totalamount float not null,
	        eventid int ,
	        exhibitorid int ,
	        PRIMARY KEY  (booking_id),
	        FOREIGN KEY (eventid) REFERENCES fair_event (event_id) ON DELETE CASCADE,
	        FOREIGN KEY (exhibitorid) REFERENCES exhibitor (exhibitor_id) ON DELETE CASCADE
	    	);
		"""

	initialise_bookingstallmap = """
	    	CREATE TABLE IF NOT EXISTS bookingstallmap (
	        id int unique auto_increment not null,
	        bookingid int ,
	        eventid int ,
	        stallid int ,
	        PRIMARY KEY  (id),
	        FOREIGN KEY (bookingid) REFERENCES booking (booking_id) ON DELETE CASCADE,
	        FOREIGN KEY (eventid) REFERENCES fair_event (event_id) ON DELETE CASCADE,
	        FOREIGN KEY (stallid) REFERENCES stall (stall_id) ON DELETE CASCADE
	    	);
		"""

	initialise_megaconsumercard ="""
	    	CREATE TABLE IF NOT EXISTS megaconsumercard (
	        id int unique auto_increment not null,
	         spend int not null,
	         spend_date date not null,
	         paymentmode varchar(255),
	         bookingid int ,
	         eventid int ,
	         visitorid int,
	         PRIMARY KEY  (id),
	         FOREIGN KEY (bookingid) REFERENCES booking (booking_id) ON DELETE CASCADE,
	         FOREIGN KEY (eventid) REFERENCES fair_event (event_id) ON DELETE CASCADE,
	         FOREIGN KEY (visitorid) REFERENCES visitor (visitor_id) ON DELETE CASCADE
	    	);
		"""

	try:
		con = db_conn.connect()
		mycursor = con.cursor()

		mycursor.execute(initialise_country)
		con.commit()

		mycursor.execute(initialise_state)
		con.commit()

		mycursor.execute(initialise_industry)
		con.commit()

		mycursor.execute(initialise_venue)
		con.commit()

		mycursor.execute(initialise_fair_event)
		con.commit()

		mycursor.execute(initialise_stall)
		con.commit()

		mycursor.execute(initialise_visitor)
		con.commit()

		mycursor.execute(initialise_exhibitor)
		con.commit()

		mycursor.execute(initialise_booking)
		con.commit()

		mycursor.execute(initialise_bookingstallmap)
		con.commit()

		mycursor.execute(initialise_megaconsumercard)
		con.commit()
		
	except Exception as e:
		print("Creation Error : ", e)
		exit()

