import os


print(os.getenv('Path'))




@app.route('/getAllRecords' , methods = ['GET'])
def get_all_records():
    req_user_name = request.args.get('username')
    req_password = request.args.get('password')
    req_dealercode = request.args.get('code')

    #req_dealer_code = request.args.get('dealercode')
    try:
        user_result = session.query(Credential).filter(Credential.userName == req_user_name).\
            filter(Credential.passWord == req_password).all()
        #dealer_result = session.query()

    except Exception as err:
        session.rollback()
        print ("err ----> ", err)
        return "error in login page"

    if user_result:
        print("i am inside if --------")
        try:
            dealer_result = session.query(Dealer).filter(Dealer.dealerCode == req_dealercode).all()
        except Exception as err:
            print("error 01 -----> ", err)

    else:
        return "dealer code not found"

    if dealer_result:
        try:
            pe_result = session.query(ProductEnquiry).all()
            convert_dict = [item.__dict__ for item in pe_result]
            for item in convert_dict:
                del item['_sa_instance_state']

            return json.dumps(convert_dict)

        except Exception as err:
            session.rollback()

        finally:
            session.close()

    else:
        return "unauthorized access"

app.run(debug = False)
