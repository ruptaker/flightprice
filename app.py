from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_price_rf.pkl","rb"))


@app.route("/")

def home():
    return render_template("home.html")


app.config['SQLALCHEMY_DAABASE_URL'] = 'postgres://lgthhmsyhhdbbs:669115d1e98675b38df24f97960f79af02b530a8ff4d63bc51c551e7df1d44a5@ec2-3-226-163-72.compute-1.amazonaws.com:5432/dadibs9r8eb5ld'

@app.route("/predict", methods = ["GET", "POST"])

def predict():
    if request.method == "POST":
        # Date_of_Journey
        Year = request.form["Year"]


        quarter = request.form["quarter"]
   

  
        airline=request.form['airline']
        if(airline=='AS'):
            AS = 1
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0

        elif (airline=='B6'):
            AS = 0
            B6 = 1
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0     
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            

        elif (airline=='CO'):
            AS = 0
            B6 = 0
            CO = 1
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            
        elif (airline=='DL'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 1       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            
        elif (airline=='F9'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 1       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            
        elif (airline=='FL'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 1       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 

        elif (airline=='G4'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 1      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 

        elif (airline=='HP'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 1       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            

        elif (airline=='NK'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 1       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            
        elif (airline=='NW'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 1       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            
        elif (airline=='Other'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 1       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 
            
        elif (airline=='TW'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 1        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 0 

        elif (airline=='UA'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 1       
            US = 0       
            WN = 0       
            YX = 0 

        elif (airline=='US'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 1       
            WN = 0       
            YX = 0 
            

        elif (airline=='WN'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 1       
            YX = 0 
            
        elif (airline=='YX'):
            AS = 0
            B6 = 0
            CO = 0
            DL = 0       
            F9 = 0       
            FL = 0       
            G4 = 0      
            HP = 0       
            NK = 0       
            NW = 0       
            Other = 0       
            TW = 0        
            UA = 0       
            US = 0       
            WN = 0       
            YX = 1 
            
        
          

##WN  = Southwest Airlines
    
#DL  =  Delta Airlines   
#AA  = American Airlines    
#UA  = United Airlines  
#US  = US airways    
#NW  = Northwest Airlines    
#CO  = Continental Airlines    
#AS  = Alaska Airlines   
#B6  = Jet Blue Airlines   
#FL  = Airtran Airways 
#G4  = Allegiant Air  
#F9  = Frontier Airlines    
#HP  = Pearl Airways      
#TW  = Tway air 
#NK  =  Spirit Airlines     
#YX  = Midwest Airlines 
#TZ  = ATA airlines
#Other      

    

     

       
       #Source 
        Source = request.form["Source"]
        if (Source == 'DepCity_Atlanta'):
           DepCity_Atlanta = 1
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0

        elif (Source == 'DepCity_Austin'):
           DepCity_Atlanta = 0
           DepCity_Austin = 1
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            

        elif (Source == 'DepCity_Boston'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 1
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            
           

        elif (Source == 'DepCity_Buffalo'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 1
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0

        elif (Source == 'DepCity_Charlotte'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 1
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            

        elif (Source == 'DepCity_Chicago'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 1
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            
           

        elif (Source == 'DepCity_Cincinnati'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 1
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0

        elif (Source == 'DepCity_Cleveland'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 1
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            

        elif (Source == 'DepCity_Columbus'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 1
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            
           

        elif (Source == 'DepCity_DallaFort'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 1
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0


           
        elif (Source == 'DepCity_Denver'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 1
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0


           
        elif (Source == 'DepCity_Detroit'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 1
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            

        elif (Source == 'DepCity_Hartford'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 1
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            
           

        elif (Source == 'DepCity_Houston'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 1 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0

        elif (Source == 'DepCity_Indianapolis'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 1
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            

        elif (Source == 'DepCity_Kansas'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 1
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            
           

        elif (Source == 'DepCity_Las'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 1
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0

        elif (Source == 'DepCity_Los'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 1 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            

        elif (Source == 'DepCity_Miami'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 1 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            
           

        elif (Source == 'DepCity_MinneapolisSt'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 1
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0


           
        elif (Source == 'DepCity_Nashville'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 1
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0

        elif (Source == 'DepCity_New'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 1
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            

        elif (Source == 'DepCity_Orlando'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 1
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 0
            
           

        elif (Source == 'DepCity_Philadelphia'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 1
           DepCity_Phoenix = 0 
           DepCity_San = 0


           
        elif (Source == 'DepCity_Phoenix'):
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 1 
           DepCity_San = 0
           
        else: 
           DepCity_Atlanta = 0
           DepCity_Austin = 0
           DepCity_Boston = 0
           DepCity_Buffalo = 0
           DepCity_Charlotte= 0
           DepCity_Chicago = 0
           DepCity_Cincinnati = 0
           DepCity_Cleveland = 0
           DepCity_Columbus = 0
           DepCity_DallasFort = 0
           DepCity_Denver = 0
           DepCity_Detroit = 0
           DepCity_Hartford = 0
           DepCity_Houston = 0 
           DepCity_Indianapolis = 0
           DepCity_Kansas = 0
           DepCity_Las = 0
           DepCity_Los = 0 
           DepCity_Miami = 0 
           DepCity_MinneapolisSt = 0
           DepCity_Nashville = 0
           DepCity_New = 0
           DepCity_Orlando = 0
           DepCity_Philadelphia = 0
           DepCity_Phoenix = 0 
           DepCity_San = 1

       
        Source = request.form["Destination"]
        if (Source == 'ArrivalCity_Las'):
             ArrivalCity_Las = 1
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0
        
        elif (Source == 'ArrivalCity_Los'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 1
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0
           

        elif (Source == 'ArrivalCity_Miami'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 1
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_MinneapolisSt'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 1
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Nashville'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 1
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Mew'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 1
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0
           

        elif (Source == 'ArrivalCity_Orlando'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 1
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Philadelphia'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 1
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Phoenix'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 1
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Pittsburgh'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 1
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0
           

        elif (Source == 'ArrivalCity_Portland'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 1
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_RaleighDurham'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 1
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Sacramento'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 1
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Salt'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 1
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_San'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 1
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0
           

        elif (Source == 'ArrivalCity_Seattle'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 1
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_St'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 1
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Tampa'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 1
             ArrivalCity_Washington = 0

        elif (Source == 'ArrivalCity_Washington'):
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 1


        else:
             ArrivalCity_Las = 0
             ArrivalCity_Los = 0
             ArrivalCity_Miami = 0
             ArrivalCity_MinneapolisSt = 0
             ArrivalCity_Nashville = 0
             ArrivalCity_New = 0
             ArrivalCity_Orlando = 0
             ArrivalCity_Philadelphia = 0
             ArrivalCity_Phoenix = 0
             ArrivalCity_Pittsburgh = 0
             ArrivalCity_Portland = 0
             ArrivalCity_RaleighDurham = 0
             ArrivalCity_Sacramento = 0
             ArrivalCity_Salt = 0
             ArrivalCity_San = 0
             ArrivalCity_Seattle = 0
             ArrivalCity_St = 0
             ArrivalCity_Tampa = 0
             ArrivalCity_Washington = 0
      

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']


    
        
        prediction=model.predict([[
            Year, 
            quarter,
            AS,
            B6,
            CO,
            DL,      
            F9,      
            FL,      
            G4,     
            HP,      
            NK,     
            NW,      
            Other,      
            TW,      
            UA,      
            US,      
            WN,      
            YX,  
            DepCity_Atlanta,
            DepCity_Austin,
            DepCity_Boston,
            DepCity_Buffalo,
            DepCity_Charlotte,
            DepCity_Chicago,
            DepCity_Cincinnati,
            DepCity_Cleveland,
            DepCity_Columbus ,
            DepCity_DallasFort,
            DepCity_Denver,
            DepCity_Detroit,
            DepCity_Hartford,
            DepCity_Houston, 
            DepCity_Indianapolis,
            DepCity_Kansas,
            DepCity_Las,
            DepCity_Los,
            DepCity_Miami,
            DepCity_MinneapolisSt,
            DepCity_Nashville,
            DepCity_New,
            DepCity_Orlando,
            DepCity_Philadelphia,
            DepCity_Phoenix,
            DepCity_San,
             ArrivalCity_Las,
             ArrivalCity_Los,
             ArrivalCity_Miami,
             ArrivalCity_MinneapolisSt,
             ArrivalCity_Nashville,
             ArrivalCity_New,
             ArrivalCity_Orlando,
             ArrivalCity_Philadelphia,
             ArrivalCity_Phoenix,
             ArrivalCity_Pittsburgh,
             ArrivalCity_Portland,
             ArrivalCity_RaleighDurham,
             ArrivalCity_Sacramento,
             ArrivalCity_Salt,
             ArrivalCity_San,
             ArrivalCity_Seattle,
             ArrivalCity_St,
             ArrivalCity_Tampa,
             ArrivalCity_Washington
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is $ {}".format(output))


    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)