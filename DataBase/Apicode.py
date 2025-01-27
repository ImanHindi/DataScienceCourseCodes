#Api Code:That allows us to send a range of GET/POST/PUT/PATCH/DELETE requests 
# We will be using the Flask framework to create our API and another separate Python file to test it.



from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)




class Users(Resource):
    # methods go here
    pass

api.add_resource(Users, '/users')  # '/users' is our entry point



class Users(Resource):
    # methods go here
    pass
    
class Locations(Resource):
    # methods go here
    pass
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations


if __name__ == '__main__':
    app.run()  # run our Flask app




class Users(Resources):
    def get(self):
        data = pd.read_csv('users.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code




parser = reqparse.RequestParser()  # initialize

parser.add_argument('userId', required=True)  # add arguments
parser.add_argument('name', required=True)
parser.add_argument('city', required=True)

args = parser.parse_args()  # parse arguments to dictionary






class Users(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })
        # read our CSV
        data = pd.read_csv('users.csv')
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv('users.csv', index=False)
        return {'data': data.to_dict()}, 200  # return data with 200 OK




# read our CSV
data = pd.read_csv('users.csv'
if args['userId'] in list(data['userId']):
    return {
        'message': f"'{args['userId']}' already exists."
    }, 401
else:
    # create new dataframe containing new values
    new_data = pd.DataFrame({
        'userId': args['userId'],
        'name': args['name'],
        'city': args['city'],
        'locations': [[]]
    })
    # add the newly provided values
    data = data.append(new_data, ignore_index=True)
    data.to_csv('users.csv', index=False)  # save back to CSV
    return {'data': data.to_dict()}, 200  # return data with 200 OK







class Users(Resource):
    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('location', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('users.csv')
        
        if args['userId'] in list(data['userId']):
            # evaluate strings of lists to lists
            data['locations'] = data['locations'].apply(
                lambda x: ast.literal_eval(x)
            )
            # select our user
            user_data = data[data['userId'] == args['userId']]

            # update user's locations
            user_data['locations'] = user_data['locations'].values[0] \
                .append(args['location'])
            
            # save back to CSV
            data.to_csv('users.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the userId does not exist
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404
