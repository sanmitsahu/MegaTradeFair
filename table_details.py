def tabledetails(tablename):
    if tablename == 'country':
        columnnames = ['Sr. No.','Country Name']
        displayquery = 'SELECT * FROM country'
        addquery = 'INSERT INTO country (countryname) VALUES (%s)'
        updatequery = 'UPDATE country SET countryname = %s WHERE country_id= %s'
        exist = 'SELECT EXISTS(SELECT * FROM country WHERE countryname=%s)'
        index = [0]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'state':
        columnnames = ['Sr. No.','State Name', 'Country Name']
        displayquery = '''SELECT state.state_id,state.statename,country.countryname 
                            FROM state
                            JOIN country 
                            ON state.countryid = country.country_id
                            ORDER BY state_id'''
        addquery = 'INSERT INTO state (statename,countryid) VALUES (%s,(SELECT country_id FROM country WHERE countryname = %s))'
        updatequery = '''UPDATE state 
                        SET 
                        statename = %s, 
                        countryid = (SELECT country_id FROM country WHERE countryname = %s)
                        WHERE state_id= %s'''
        exist = 'SELECT EXISTS(SELECT * FROM state WHERE statename=%s)'
        index = [0]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'industry':
        columnnames = ['Sr. No.','Industry Name']
        displayquery = 'SELECT * FROM industry'
        addquery = 'INSERT INTO industry (industryname) VALUES (%s)'
        updatequery = 'UPDATE industry SET industryname = %s WHERE industry_id= %s'
        exist = 'SELECT EXISTS(SELECT * FROM industry WHERE industryname=%s)'
        index = [0]
        return columnnames,displayquery,addquery,updatequery, exist, index
    
    elif tablename == 'venue':
        columnnames = ['Sr. No.','City Name', 'Address', 'Country Name', 'State Name']
        displayquery = '''SELECT venue.venue_id, venue.cityname, venue.address, country.countryname, state.statename
                            FROM venue
                            JOIN state ON venue.stateid = state.state_id
                            JOIN country ON venue.countryid = country.country_id
                            ORDER BY venue_id'''
        addquery = '''INSERT INTO venue (cityname, address, countryid, stateid) 
                    VALUES (%s, %s, (SELECT country_id FROM country WHERE countryname = %s),
                    (SELECT state_id FROM state WHERE statename = %s))'''
        updatequery = '''UPDATE venue SET 
                        venuename = %s,
                        address = %s,
                        countryid = (SELECT country_id FROM country WHERE countryname = %s),
                        stateid = (SELECT state_id FROM state WHERE statename = %s)
                        WHERE venue_id=%s'''
        exist = 'SELECT EXISTS(SELECT * FROM venue WHERE cityname=%s)'
        index = [0]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'stall':
        columnnames = ['Sr. No.','Stall No.', 'Price', 'Stall Size', 'Booking status', 'Event Name']
        displayquery = '''SELECT stall.stall_id, stall.stallno, stall.price, stall.stallsize, stall.isbooked, fair_event.event_name 
                        FROM stall
                        JOIN fair_event ON stall.eventid = fair_event.event_id
                        ORDER BY stall.stall_id'''
        addquery = '''INSERT INTO stall (stallno, price, stallsize, isbooked, eventid) 
                    VALUES (%s, %s, %s, %s, (SELECT event_id FROM fair_event WHERE event_name=%s))'''
        updatequery = '''UPDATE stall SET 
                        stallno = %s,
                        price = %s,
                        stallsize = %s,
                        isbooked = %s,
                        eventid = (SELECT event_id FROM fair_event WHERE event_name = %s) WHERE stall_id=%s'''
        
        exist = 'SELECT EXISTS(SELECT * FROM stall WHERE stallno=%s)'
        index = [0]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'fair_event':
        columnnames = ['Sr. No.', 'Event Name', 'Booking starts', 'Start Date', 'End date', 'Venu']
        displayquery = '''SELECT fair_event.event_id, fair_event.event_name, fair_event.bookingstartdate, fair_event.startdate, fair_event.enddate, venue.cityname
                        FROM fair_event
                        JOIN venue ON fair_event.venueid = venue.venue_id
                        ORDER BY fair_event.event_id'''
        addquery = '''INSERT INTO fair_event (event_name, bookingstartdate, startdate, enddate, venueid) 
                    VALUES (%s, %s, %s, %s, (SELECT venue_id FROM venue WHERE cityname = %s))''' 
        updatequery = '''UPDATE fair_event SET 
                        event_name = %s,
                        bookingstartdate = %s, 
                        startdate = %s,
                        enddate = %s,
                        venueid = (SELECT venue_id FROM venue WHERE cityname = %s) WHERE event_id=%s'''
        exist = 'SELECT EXISTS(SELECT * FROM fair_event WHERE event_name=%s and venueid=(SELECT venue_id FROM venue WHERE cityname = %s))'
        index = [0, 4]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'megaconsumercard':
        columnnames = ['Sr. No.', 'Amount spend', 'Spend Date', 'Payment Mode', 'booking id', 'Event name', 'Visitor name']
        displayquery = '''SELECT megaconsumercard.id, megaconsumercard.spend, megaconsumercard.spend_date, megaconsumercard.paymentmode, megaconsumercard.bookingid, fair_event.event_name, visitor.firstname
                        FROM megaconsumercard
                        JOIN fair_event ON megaconsumercard.eventid = fair_event.event_id
                        JOIN visitor ON megaconsumercard.visitorid = visitor.visitor_id
                        ORDER BY megaconsumercard.id'''
        addquery = '''INSERT INTO megaconsumercard (spend, spend_date, paymentmode, bookingid, eventid, visitorid) 
                    VALUES (%s, %s, %s, %s, (SELECT event_id FROM fair_event WHERE event_name = %s),
                                            (SELECT visitor_id FROM visitor WHERE firstname=%s))'''
        updatequery = '''UPDATE megaconsumercard SET 
                        spend=%s, 
                        spend_date=%s, 
                        paymentmode=%s, 
                        bookingid=%s, 
                        eventid=(SELECT event_id FROM fair_event WHERE event_name = %s), 
                        visitorid=(SELECT visitor_id FROM visitor WHERE firstname=%s)
                        WHERE id=%s'''
        exist = '''SELECT EXISTS(SELECT * FROM megaconsumercard WHERE bookingid=%s
                 and eventid=(SELECT event_id FROM fair_event WHERE event_name = %s) 
                 and visitorid=(SELECT visitor_id FROM visitor WHERE firstname=%s))'''
        index = [3, 4, 5]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'visitor':
        columnnames = ['Sr. No','First Name','Last Name','Address','Pincode','MobileNo','EmailId','Date-Of-Birth','Gender']
        displayquery = 'SELECT * FROM visitor'
        addquery = """INSERT INTO visitor (firstname, lastname, address, pincode, mobileno, email_id, dateofbirth, 
                   gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s); """
        updatequery = """UPDATE visitor SET  `firstname`=%s, `lastname`=%s, `address`=%s,`pincode`=%s,`mobileno`=%s,`email_id`=%s,
                      `dateofbirth`=%s,`gender`= %s 
                      WHERE `visitor`.visitor_id=%s;"""
        return columnnames,displayquery,addquery,updatequery

    elif tablename == 'exhibitor':
        columnnames=['Sr. No','Exhibitor Name','Email Id','PhoneNo','Company Name','Company Description','Address','Pincode','Industry Name','Country Name','State Name']
        displayquery = """SELECT  `exhibitor_id`,`exhibitorname`,`email_id`,`phoneno`,`companyname`,`companydescription`,`address`,`pincode`,
                            `industry`.industryname,`country`.countryname,`state`.statename
                            FROM exhibitor 
                            INNER JOIN
                            `country` ON `country`.country_id=`exhibitor`.countryid
                            INNER JOIN
                            `industry` ON `industry`.industry_id=`exhibitor`.industryid
                            INNER JOIN
                            `state` ON `state`.state_id=`exhibitor`.stateid;"""
        addquery = """INSERT INTO exhibitor (`exhibitorname`,`email_id`,`phoneno`,`companyname`,`companydescription`,`address`,`pincode`,industryid,countryid,stateid) VALUES (%s,%s,%s,%s,%s,%s,%s,(SELECT industry_id FROM industry WHERE industryname = %s),
                    (SELECT `country_id` FROM `country` WHERE `countryname` = %s),
                    (SELECT `state_id` FROM `state` WHERE `statename` = %s));"""
        updatequery = """UPDATE  `exhibitor`
                        SET `exhibitorname`=%s,`email_id`=%s,`phoneno`=%s,`companyname`=%s,`companydescription`=%s,`address`=%s,`pincode`=%s,
                        industryid = (SELECT industry_id FROM industry WHERE industryname = %s),
                        countryid = (SELECT country_id FROM country WHERE countryname = %s),
                        stateid = (SELECT state_id FROM state WHERE statename = %s)
                        WHERE exhibitor_id= %s"""
        exist = 'SELECT EXISTS(SELECT * FROM exhibitor WHERE exhibitorname=%s and companyname=%s and industryid = (SELECT industry_id FROM industry WHERE industryname = %s))'
        index = [0, 3, 7] 
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'booking':
        columnnames=['Sr. No','Booking Date','Total Amount','Event Name','Exhibitor Name']
        displayquery = """SELECT `booking_id`,`bookingdate`,`totalamount`,`fair_event`.event_name,`exhibitor`.exhibitorname
                            FROM booking 
                            INNER JOIN
                            `fair_event` ON `fair_event`.event_id=`booking`.eventid
                            INNER JOIN
                            `exhibitor` ON `exhibitor`.exhibitor_id=`booking`.exhibitorid;
                            """
        addquery = """INSERT INTO booking (`bookingdate`,`totalamount`,`eventid`,`exhibitorid`) 
                        VALUES (%s,%s,(SELECT event_id FROM fair_event WHERE event_name = %s),(SELECT exhibitor_id FROM exhibitor WHERE exhibitorname = %s));"""
        updatequery = """UPDATE  `booking`
                        SET `bookingdate`=%s,`totalamount`=%s,
                        eventid = (SELECT event_id FROM fair_event WHERE event_name = %s),
                        exhibitorid = (SELECT exhibitor_id FROM exhibitor WHERE exhibitorname = %s)
                        WHERE booking_id= %s"""
        exist = '''SELECT EXISTS(SELECT * FROM booking WHERE eventid = (SELECT event_id FROM fair_event WHERE event_name = %s),
                        exhibitorid = (SELECT exhibitor_id FROM exhibitor WHERE exhibitorname = %s))'''
        index = [2, 3]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'bookingstallmap':
        columnnames=['Sr. No','Booking Total Amount','Event Name','Stall Price']
        addquery = """INSERT INTO bookingstallmap (`bookingid`,`eventid`,`stallid`) 
                        VALUES ((SELECT booking_id FROM booking WHERE totalamount = %s),(SELECT event_id FROM fair_event WHERE event_name = %s),(SELECT stall_id FROM stall WHERE price = %s));"""
        displayquery = """SELECT  id,`booking`.`totalamount`,`fair_event`.`event_name`,`stall`.`price`
                            FROM bookingstallmap
                            INNER JOIN
                            `booking` ON `booking`.booking_id = `bookingstallmap`.bookingid
                            INNER JOIN
                            `fair_event` ON `fair_event`.event_id=`bookingstallmap`.eventid
                            INNER JOIN
                            `stall` ON `stall`.stall_id=`bookingstallmap`.stallid;
                            """
        updatequery = """UPDATE  `bookingstallmap`
                        SET bookingid = (SELECT booking_id FROM booking WHERE totalamount = %s), 
                        eventid = (SELECT event_id FROM fair_event WHERE event_name = %s),
                        stallid = (SELECT stall_id FROM stall WHERE price = %s)
                        WHERE id= %s"""
        exist = '''SELECT EXISTS(SELECT * FROM bookingstallmap WHERE bookingid = (SELECT booking_id FROM booking WHERE totalamount = %s), 
                        eventid = (SELECT event_id FROM fair_event WHERE event_name = %s),
                        stallid = (SELECT stall_id FROM stall WHERE price = %s))'''
        index = [0, 1, 2]
        return columnnames,displayquery,addquery,updatequery, exist, index

    elif tablename == 'bookingdashboard':
        columnnames=['Booking Date','Booking Amount','Exhibitor Name','Company Name','Exhibitor Contact','Address','Event Name','City','State','Country']
        displayquery = """SELECT  `booking`.`bookingdate`,`booking`.`totalamount`,`exhibitor`.`exhibitorname`,`exhibitor`.`companyname`,`exhibitor`.`phoneno`,`exhibitor`.`address`,`fair_event`.`event_name`,`venue`.`cityname`,`state`.`statename`,`country`.`countryname`
                            FROM booking 
                            INNER JOIN
                            `fair_event` ON `fair_event`.event_id=`booking`.eventid
                            INNER JOIN
                            `exhibitor` ON `exhibitor`.exhibitor_id=`booking`.exhibitorid
                            INNER JOIN
                            `venue` ON `venue`.venue_id=`fair_event`.venueid
                            INNER JOIN
                            `state` ON `state`.state_id=`venue`.stateid
                            INNER JOIN
                            `country` ON `country`.country_id=`state`.countryid;"""

        return columnnames,displayquery

    elif tablename == 'industrybooking':
        columnnames = ['Industry Name', 'Total Exhibitors', 'Total Amount']
        displayquery = """SELECT industry.industryname, count(*), sum(totalamount)
                        FROM industry
                        JOIN exhibitor ON industry.industry_id = exhibitor.industryid
                        JOIN booking ON exhibitor.exhibitor_id = booking.exhibitorid
                        GROUP BY industry.industry_id;"""
        return columnnames,displayquery
    
    
    elif tablename == 'industrybusiness':
        columnnames = ['Industry Name','Amount Earned','Amount Spent','Number of Visitors']
        displayquery = """SELECT industryname, sum(spend), sum(totalamount) , count(visitor_id)
                        FROM industry
                        JOIN exhibitor
                        ON industry.industry_id = exhibitor.industryid
                        JOIN booking
                        ON exhibitor.exhibitor_id = booking.exhibitorid
                        JOIN megaconsumercard
                        ON booking.booking_id = megaconsumercard.bookingid
                        JOIN visitor
                        ON megaconsumercard.visitorid = visitor.visitor_id;"""
        return columnnames,displayquery
