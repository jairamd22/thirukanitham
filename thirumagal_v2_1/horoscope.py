import sys
import os
import math
import datetime
from dateutil.relativedelta import relativedelta

def get_planet_degree(longitude):
    signs = ["MESHAM", "RISHABAM", "MITHUNAM", "KADAGAM", "SIMMAM", "KANNI", "THULAM", "VIRUCHIGAM", "DHANUSU", "MAGARAM", "KUMBAM", "MEENAM"]
  
    #for x in signs:
    #   print(x)

    sign_num = math.floor(longitude / 30)
    pos_in_sign = longitude - (sign_num * 30)
    deg = math.floor(pos_in_sign)
    full_min = (pos_in_sign - deg) * 60
    min = math.floor(full_min)
    full_sec = round((full_min - min) * 60)
    
    #print(sign_num)
    #print(pos_in_sign)
    #print(deg)
    #print(full_min)
    #print(min)
    #print(full_sec)
    
    if deg < 10:
        deg = str(0) + str(deg)

    if min < 10:
        min = str(0) + str(min)

    if full_sec < 10:
        full_sec = str(0) + str(full_sec)

    return str(deg) + ":" + str(min) + ":" + str(full_sec);
    
    

def get_planet_house(longitude):
    signs = ["MESHAM", "RISHABAM", "MITHUNAM", "KADAGAM", "SIMMAM", "KANNI", "THULAM", "VIRUCHIGAM", "DHANUSU", "MAGARAM", "KUMBAM", "MEENAM"]
    
    #signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]  
    #for x in signs:
    #   print(x)

    sign_num = math.floor(longitude / 30)
    pos_in_sign = longitude - (sign_num * 30)
    deg = math.floor(pos_in_sign)
    full_min = (pos_in_sign - deg) * 60
    min = math.floor(full_min)
    full_sec = round((full_min - min) * 60)
    
    #print(sign_num)
    #print(pos_in_sign)
    #print(deg)
    #print(full_min)
    #print(min)
    #print(full_sec)
    
    if deg < 10:
        deg = str(0) + str(deg)

    if min < 10:
        min = str(0) + str(min)

    if full_sec < 10:
        full_sec = str(0) + str(full_sec)

    return signs[sign_num]
       
       
def get_planet_house_english(longitude):
    #signs = ["MESHAM", "RISHABAM", "MITHUNAM", "KADAGAM", "SIMMAM", "KANNI", "THULAM", "VIRUCHIGAM", "DHANUSU", "MAGARAM", "KUMBAM", "MEENAM"]
    
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]  
    #for x in signs:
    #   print(x)

    sign_num = math.floor(longitude / 30)
    pos_in_sign = longitude - (sign_num * 30)
    deg = math.floor(pos_in_sign)
    full_min = (pos_in_sign - deg) * 60
    min = math.floor(full_min)
    full_sec = round((full_min - min) * 60)
    
    #print(sign_num)
    #print(pos_in_sign)
    #print(deg)
    #print(full_min)
    #print(min)
    #print(full_sec)
    
    if deg < 10:
        deg = str(0) + str(deg)

    if min < 10:
        min = str(0) + str(min)

    if full_sec < 10:
        full_sec = str(0) + str(full_sec)

    return signs[sign_num]
    
    
def get_planet_house_tamil(longitude):
    signs = ["மேஷம்", "ரிஷபம்", "மிதுனம்", "கடகம்", "சிம்மம்", "கன்னி", "துலாம்", "விருச்சிகம்", "தனுசு", "மகரம்", "கும்பம்", "மீனம்"]
    
    #signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]  
    #for x in signs:
    #   print(x)

    sign_num = math.floor(longitude / 30)
    pos_in_sign = longitude - (sign_num * 30)
    deg = math.floor(pos_in_sign)
    full_min = (pos_in_sign - deg) * 60
    min = math.floor(full_min)
    full_sec = round((full_min - min) * 60)
    
    #print(sign_num)
    #print(pos_in_sign)
    #print(deg)
    #print(full_min)
    #print(min)
    #print(full_sec)
    
    if deg < 10:
        deg = str(0) + str(deg)

    if min < 10:
        min = str(0) + str(min)

    if full_sec < 10:
        full_sec = str(0) + str(full_sec)

    return signs[sign_num]
    
       
def Convert_Longitude_into_time(longitude):
    tdeg = math.floor(longitude);
    pos_in_sign = longitude - tdeg;
    deg = math.floor(pos_in_sign);
    full_min = (pos_in_sign - deg) * 60;
    min = math.floor(full_min);
    full_sec = round((full_min - min) * 60);
    return str(tdeg) + ":" + str(min) + ":" + str(full_sec);


def star_query(deg):
    if deg > 0 and deg <= 3.333333333:
        star="ASWINI"
    elif deg > 3.333333333 and deg <= 6.666666667:
        star="ASWINI"
    elif deg > 6.666666667 and deg <= 10:
        star="ASWINI"
    elif deg > 10 and deg <= 13.33333333:
        star="ASWINI"
    elif deg > 13.33333333 and deg <= 16.66666667:
        star="BHARANI"
    elif deg > 16.66666667 and deg <= 20:
        star="BHARANI"
    elif deg > 20 and deg <= 23.33333333:
        star="BHARANI"
    elif deg > 23.33333333 and deg <= 26.66666667:
        star="BHARANI"
    elif deg > 26.66666667 and deg <= 30:
        star="KIRUTHIGAI"
    elif deg > 30 and deg <= 33.33333333:
        star="KIRUTHIGAI"
    elif deg > 33.33333333 and deg <= 36.66666667:
        star="KIRUTHIGAI"
    elif deg > 36.66666667 and deg <= 40:
        star="KIRUTHIGAI"
    elif deg > 40 and deg <= 43.33333333:
        star="ROGINI"
    elif deg > 43.33333333 and deg <= 46.66666667:
        star="ROGINI"
    elif deg > 46.66666667 and deg <= 50:
        star="ROGINI"
    elif deg > 50 and deg <= 53.33333333:
        star="ROGINI"
    elif deg > 53.33333333 and deg <= 56.66666667:
        star="MIRUGASEERASAM"
    elif deg > 56.66666667 and deg <= 60:
        star="MIRUGASEERASAM"
    elif deg > 60 and deg <= 63.33333333:
        star="MIRUGASEERASAM"
    elif deg > 63.33333333 and deg <= 66.66666667:
        star="MIRUGASEERASAM"
    elif deg > 66.66666667 and deg <= 70:
        star="THIRUVAADHIRAI"
    elif deg > 70 and deg <= 73.33333333:
        star="THIRUVAADHIRAI"
    elif deg > 73.33333333 and deg <= 76.66666667:
        star="THIRUVAADHIRAI"
    elif deg > 76.66666667 and deg <= 80:
        star="THIRUVAADHIRAI"
    elif deg > 80 and deg <= 83.33333333:
        star="PUNARPOOSAM"
    elif deg > 83.33333333 and deg <= 86.66666667:
        star="PUNARPOOSAM"
    elif deg > 86.66666667 and deg <= 90:
        star="PUNARPOOSAM"
    elif deg > 90 and deg <= 93.33333333:
        star="PUNARPOOSAM"
    elif deg > 93.33333333 and deg <= 96.66666667:
        star="POOSAM"
    elif deg > 96.66666667 and deg <= 100:
        star="POOSAM"
    elif deg > 100 and deg <= 103.3333333:
        star="POOSAM"
    elif deg > 103.3333333 and deg <= 106.6666667:
        star="POOSAM"
    elif deg > 106.6666667 and deg <= 110:
        star="AYILYAM"
    elif deg > 110 and deg <= 113.3333333:
        star="AYILYAM"
    elif deg > 113.3333333 and deg <= 116.6666667:
        star="AYILYAM"
    elif deg > 116.6666667 and deg <= 120:
        star="AYILYAM"
    elif deg > 120 and deg <= 123.3333333:
        star="MAGAM"
    elif deg > 123.3333333 and deg <= 126.6666667:
        star="MAGAM"
    elif deg > 126.6666667 and deg <= 130:
        star="MAGAM"
    elif deg > 130 and deg <= 133.3333333:
        star="MAGAM"
    elif deg > 133.3333333 and deg <= 136.6666667:
        star="POORAM"
    elif deg > 136.6666667 and deg <= 140:
        star="POORAM"
    elif deg > 140 and deg <= 143.3333333:
        star="POORAM"
    elif deg > 143.3333333 and deg <= 146.6666667:
        star="POORAM"
    elif deg > 146.6666667 and deg <= 150:
        star="UTHRAM"
    elif deg > 150 and deg <= 153.3333333:
        star="UTHRAM"
    elif deg > 153.3333333 and deg <= 156.6666667:
        star="UTHRAM"
    elif deg > 156.6666667 and deg <= 160:
        star="UTHRAM"
    elif deg > 160 and deg <= 163.3333333:
        star="HASTHAM"
    elif deg > 163.3333333 and deg <= 166.6666667:
        star="HASTHAM"
    elif deg > 166.6666667 and deg <= 170:
        star="HASTHAM"
    elif deg > 170 and deg <= 173.3333333:
        star="HASTHAM"
    elif deg > 173.3333333 and deg <= 176.6666667:
        star="SITHIRAI"
    elif deg > 176.6666667 and deg <= 180:
        star="SITHIRAI"
    elif deg > 180 and deg <= 183.3333333:
        star="SITHIRAI"
    elif deg > 183.3333333 and deg <= 186.6666667:
        star="SITHIRAI"
    elif deg > 186.6666667 and deg <= 190:
        star="SUVATHI"
    elif deg > 190 and deg <= 193.3333333:
        star="SUVATHI"
    elif deg > 193.3333333 and deg <= 196.6666667:
        star="SUVATHI"
    elif deg > 196.6666667 and deg <= 200:
        star="SUVATHI"
    elif deg > 200 and deg <= 203.3333333:
        star="VISAAGAM"
    elif deg > 203.3333333 and deg <= 206.6666667:
        star="VISAAGAM"
    elif deg > 206.6666667 and deg <= 210:
        star="VISAAGAM"
    elif deg > 210 and deg <= 213.3333333:
        star="VISAAGAM"
    elif deg > 213.3333333 and deg <= 216.6666667:
        star="ANUSAM"
    elif deg > 216.6666667 and deg <= 220:
        star="ANUSAM"
    elif deg > 220 and deg <= 223.3333333:
        star="ANUSAM"
    elif deg > 223.3333333 and deg <= 226.6666667:
        star="ANUSAM"
    elif deg > 226.6666667 and deg <= 230:
        star="KETTAI"
    elif deg > 230 and deg <= 233.3333333:
        star="KETTAI"
    elif deg > 233.3333333 and deg <= 236.6666667:
        star="KETTAI"
    elif deg > 236.6666667 and deg <= 240:
        star="KETTAI"
    elif deg > 240 and deg <= 243.3333333:
        star="MOOLAM"
    elif deg > 243.3333333 and deg <= 246.6666667:
        star="MOOLAM"
    elif deg > 246.6666667 and deg <= 250:
        star="MOOLAM"
    elif deg > 250 and deg <= 253.3333333:
        star="MOOLAM"
    elif deg > 253.3333333 and deg <= 256.6666667:
        star="POORAADAM"
    elif deg > 256.6666667 and deg <= 260:
        star="POORAADAM"
    elif deg > 260 and deg <= 263.3333333:
        star="POORAADAM"
    elif deg > 263.3333333 and deg <= 266.6666667:
        star="POORAADAM"
    elif deg > 266.6666667 and deg <= 270:
        star="UTHIRAADAM"
    elif deg > 270 and deg <= 273.3333333:
        star="UTHIRAADAM"
    elif deg > 273.3333333 and deg <= 276.6666667:
        star="UTHIRAADAM"
    elif deg > 276.6666667 and deg <= 280:
        star="UTHIRAADAM"
    elif deg > 280 and deg <= 283.3333333:
        star="THIRUVONAM"
    elif deg > 283.3333333 and deg <= 286.6666667:
        star="THIRUVONAM"
    elif deg > 286.6666667 and deg <= 290:
        star="THIRUVONAM"
    elif deg > 290 and deg <= 293.3333333:
        star="THIRUVONAM"
    elif deg > 23.3333333 and deg <= 296.6666667:
        star="AVITTAM"
    elif deg > 296.6666667 and deg <= 300:
        star="AVITTAM"
    elif deg > 300 and deg <= 303.3333333:
        star="AVITTAM"
    elif deg > 303.3333333 and deg <= 306.6666667:
        star="AVITTAM"
    elif deg > 306.6666667 and deg <= 310:
        star="SADAYAM"
    elif deg > 310 and deg <= 313.3333333:
        star="SADAYAM"
    elif deg > 313.3333333 and deg <= 316.6666667:
        star="SADAYAM"
    elif deg > 316.6666667 and deg <= 320:
        star="SADAYAM"
    elif deg > 320 and deg <= 323.3333333:
        star="POORATTAADHI"
    elif deg > 323.3333333 and deg <= 326.6666667:
        star="POORATTAADHI"
    elif deg > 326.6666667 and deg <= 330:
        star="POORATTAADHI"
    elif deg > 330 and deg <= 333.3333333:
        star="POORATTAADHI"
    elif deg > 333.3333333 and deg <= 336.6666667:
        star="UTHRATTAADHI"
    elif deg > 336.6666667 and deg <= 340:
        star="UTHRATTAADHI"
    elif deg > 340 and deg <= 343.3333333:
        star="UTHRATTAADHI"
    elif deg > 343.3333333 and deg <= 346.6666667:
        star="UTHRATTAADHI"
    elif deg > 346.6666667 and deg <= 350:
        star="REVATHI"
    elif deg > 350 and deg <= 353.3333333:
        star="REVATHI"
    elif deg > 353.3333333 and deg <= 356.6666667:
        star="REVATHI"
    elif deg > 356.6666667 and deg <= 360:
        star="REVATHI"
    
    return star

def star_query_tamil(deg):
    if deg > 0 and deg <= 3.333333333:
        star="அஸ்வினி"
    elif deg > 3.333333333 and deg <= 6.666666667:
        star="அஸ்வினி"
    elif deg > 6.666666667 and deg <= 10:
        star="அஸ்வினி"
    elif deg > 10 and deg <= 13.33333333:
        star="அஸ்வினி"
    elif deg > 13.33333333 and deg <= 16.66666667:
        star="பரணி"
    elif deg > 16.66666667 and deg <= 20:
        star="பரணி"
    elif deg > 20 and deg <= 23.33333333:
        star="பரணி"
    elif deg > 23.33333333 and deg <= 26.66666667:
        star="பரணி"
    elif deg > 26.66666667 and deg <= 30:
        star="கார்த்திகை"
    elif deg > 30 and deg <= 33.33333333:
        star="கார்த்திகை"
    elif deg > 33.33333333 and deg <= 36.66666667:
        star="கார்த்திகை"
    elif deg > 36.66666667 and deg <= 40:
        star="கார்த்திகை"
    elif deg > 40 and deg <= 43.33333333:
        star="ரோகிணி"
    elif deg > 43.33333333 and deg <= 46.66666667:
        star="ரோகிணி"
    elif deg > 46.66666667 and deg <= 50:
        star="ரோகிணி"
    elif deg > 50 and deg <= 53.33333333:
        star="ரோகிணி"
    elif deg > 53.33333333 and deg <= 56.66666667:
        star="மிருகசீரிடம்"
    elif deg > 56.66666667 and deg <= 60:
        star="மிருகசீரிடம்"
    elif deg > 60 and deg <= 63.33333333:
        star="மிருகசீரிடம்"
    elif deg > 63.33333333 and deg <= 66.66666667:
        star="மிருகசீரிடம்"
    elif deg > 66.66666667 and deg <= 70:
        star="திருவாதிரை"
    elif deg > 70 and deg <= 73.33333333:
        star="திருவாதிரை"
    elif deg > 73.33333333 and deg <= 76.66666667:
        star="திருவாதிரை"
    elif deg > 76.66666667 and deg <= 80:
        star="திருவாதிரை"
    elif deg > 80 and deg <= 83.33333333:
        star="புனர்பூசம்"
    elif deg > 83.33333333 and deg <= 86.66666667:
        star="புனர்பூசம்"
    elif deg > 86.66666667 and deg <= 90:
        star="புனர்பூசம்"
    elif deg > 90 and deg <= 93.33333333:
        star="புனர்பூசம்"
    elif deg > 93.33333333 and deg <= 96.66666667:
        star="பூசம்"
    elif deg > 96.66666667 and deg <= 100:
        star="பூசம்"
    elif deg > 100 and deg <= 103.3333333:
        star="பூசம்"
    elif deg > 103.3333333 and deg <= 106.6666667:
        star="பூசம்"
    elif deg > 106.6666667 and deg <= 110:
        star="ஆயில்யம்"
    elif deg > 110 and deg <= 113.3333333:
        star="ஆயில்யம்"
    elif deg > 113.3333333 and deg <= 116.6666667:
        star="ஆயில்யம்"
    elif deg > 116.6666667 and deg <= 120:
        star="ஆயில்யம்"
    elif deg > 120 and deg <= 123.3333333:
        star="மகம்"
    elif deg > 123.3333333 and deg <= 126.6666667:
        star="மகம்"
    elif deg > 126.6666667 and deg <= 130:
        star="மகம்"
    elif deg > 130 and deg <= 133.3333333:
        star="மகம்"
    elif deg > 133.3333333 and deg <= 136.6666667:
        star="பூரம்"
    elif deg > 136.6666667 and deg <= 140:
        star="பூரம்"
    elif deg > 140 and deg <= 143.3333333:
        star="பூரம்"
    elif deg > 143.3333333 and deg <= 146.6666667:
        star="பூரம்"
    elif deg > 146.6666667 and deg <= 150:
        star="உத்திரம்"
    elif deg > 150 and deg <= 153.3333333:
        star="உத்திரம்"
    elif deg > 153.3333333 and deg <= 156.6666667:
        star="உத்திரம்"
    elif deg > 156.6666667 and deg <= 160:
        star="உத்திரம்"
    elif deg > 160 and deg <= 163.3333333:
        star="ஹஸ்தம்"
    elif deg > 163.3333333 and deg <= 166.6666667:
        star="ஹஸ்தம்"
    elif deg > 166.6666667 and deg <= 170:
        star="ஹஸ்தம்"
    elif deg > 170 and deg <= 173.3333333:
        star="ஹஸ்தம்"
    elif deg > 173.3333333 and deg <= 176.6666667:
        star="சித்திரை"
    elif deg > 176.6666667 and deg <= 180:
        star="சித்திரை"
    elif deg > 180 and deg <= 183.3333333:
        star="சித்திரை"
    elif deg > 183.3333333 and deg <= 186.6666667:
        star="சித்திரை"
    elif deg > 186.6666667 and deg <= 190:
        star="சுவாதி"
    elif deg > 190 and deg <= 193.3333333:
        star="சுவாதி"
    elif deg > 193.3333333 and deg <= 196.6666667:
        star="சுவாதி"
    elif deg > 196.6666667 and deg <= 200:
        star="சுவாதி"
    elif deg > 200 and deg <= 203.3333333:
        star="விசாகம்"
    elif deg > 203.3333333 and deg <= 206.6666667:
        star="விசாகம்"
    elif deg > 206.6666667 and deg <= 210:
        star="விசாகம்"
    elif deg > 210 and deg <= 213.3333333:
        star="விசாகம்"
    elif deg > 213.3333333 and deg <= 216.6666667:
        star="அனுசம்"
    elif deg > 216.6666667 and deg <= 220:
        star="அனுசம்"
    elif deg > 220 and deg <= 223.3333333:
        star="அனுசம்"
    elif deg > 223.3333333 and deg <= 226.6666667:
        star="அனுசம்"
    elif deg > 226.6666667 and deg <= 230:
        star="கேட்டை"
    elif deg > 230 and deg <= 233.3333333:
        star="கேட்டை"
    elif deg > 233.3333333 and deg <= 236.6666667:
        star="கேட்டை"
    elif deg > 236.6666667 and deg <= 240:
        star="கேட்டை"
    elif deg > 240 and deg <= 243.3333333:
        star="மூலம்"
    elif deg > 243.3333333 and deg <= 246.6666667:
        star="மூலம்"
    elif deg > 246.6666667 and deg <= 250:
        star="மூலம்"
    elif deg > 250 and deg <= 253.3333333:
        star="மூலம்"
    elif deg > 253.3333333 and deg <= 256.6666667:
        star="பூராடம்"
    elif deg > 256.6666667 and deg <= 260:
        star="பூராடம்"
    elif deg > 260 and deg <= 263.3333333:
        star="பூராடம்"
    elif deg > 263.3333333 and deg <= 266.6666667:
        star="பூராடம்"
    elif deg > 266.6666667 and deg <= 270:
        star="உத்திராடம்"
    elif deg > 270 and deg <= 273.3333333:
        star="உத்திராடம்"
    elif deg > 273.3333333 and deg <= 276.6666667:
        star="உத்திராடம்"
    elif deg > 276.6666667 and deg <= 280:
        star="உத்திராடம்"
    elif deg > 280 and deg <= 283.3333333:
        star="திருவோணம்"
    elif deg > 283.3333333 and deg <= 286.6666667:
        star="திருவோணம்"
    elif deg > 286.6666667 and deg <= 290:
        star="திருவோணம்"
    elif deg > 290 and deg <= 293.3333333:
        star="திருவோணம்"
    elif deg > 23.3333333 and deg <= 296.6666667:
        star="அவிட்டம்"
    elif deg > 296.6666667 and deg <= 300:
        star="அவிட்டம்"
    elif deg > 300 and deg <= 303.3333333:
        star="அவிட்டம்"
    elif deg > 303.3333333 and deg <= 306.6666667:
        star="அவிட்டம்"
    elif deg > 306.6666667 and deg <= 310:
        star="சதயம்"
    elif deg > 310 and deg <= 313.3333333:
        star="சதயம்"
    elif deg > 313.3333333 and deg <= 316.6666667:
        star="சதயம்"
    elif deg > 316.6666667 and deg <= 320:
        star="சதயம்"
    elif deg > 320 and deg <= 323.3333333:
        star="பூரட்டாதி"
    elif deg > 323.3333333 and deg <= 326.6666667:
        star="பூரட்டாதி"
    elif deg > 326.6666667 and deg <= 330:
        star="பூரட்டாதி"
    elif deg > 330 and deg <= 333.3333333:
        star="பூரட்டாதி"
    elif deg > 333.3333333 and deg <= 336.6666667:
        star="உத்திரட்டாதி"
    elif deg > 336.6666667 and deg <= 340:
        star="உத்திரட்டாதி"
    elif deg > 340 and deg <= 343.3333333:
        star="உத்திரட்டாதி"
    elif deg > 343.3333333 and deg <= 346.6666667:
        star="உத்திரட்டாதி"
    elif deg > 346.6666667 and deg <= 350:
        star="ரேவதி"
    elif deg > 350 and deg <= 353.3333333:
        star="ரேவதி"
    elif deg > 353.3333333 and deg <= 356.6666667:
        star="ரேவதி"
    elif deg > 356.6666667 and deg <= 360:
        star="ரேவதி"
    
    return star
    
    
def star_query_english(deg):
    if deg > 0 and deg <= 3.333333333:
        star="Ashvini"
    elif deg > 3.333333333 and deg <= 6.666666667:
        star="Ashvini"
    elif deg > 6.666666667 and deg <= 10:
        star="Ashvini"
    elif deg > 10 and deg <= 13.33333333:
        star="Ashvini"
    elif deg > 13.33333333 and deg <= 16.66666667:
        star="Bharani"
    elif deg > 16.66666667 and deg <= 20:
        star="Bharani"
    elif deg > 20 and deg <= 23.33333333:
        star="Bharani"
    elif deg > 23.33333333 and deg <= 26.66666667:
        star="Bharani"
    elif deg > 26.66666667 and deg <= 30:
        star="Krittika"
    elif deg > 30 and deg <= 33.33333333:
        star="Krittika"
    elif deg > 33.33333333 and deg <= 36.66666667:
        star="Krittika"
    elif deg > 36.66666667 and deg <= 40:
        star="Krittika"
    elif deg > 40 and deg <= 43.33333333:
        star="Rohini"
    elif deg > 43.33333333 and deg <= 46.66666667:
        star="Rohini"
    elif deg > 46.66666667 and deg <= 50:
        star="Rohini"
    elif deg > 50 and deg <= 53.33333333:
        star="Rohini"
    elif deg > 53.33333333 and deg <= 56.66666667:
        star="Mrigashirsha"
    elif deg > 56.66666667 and deg <= 60:
        star="Mrigashirsha"
    elif deg > 60 and deg <= 63.33333333:
        star="Mrigashirsha"
    elif deg > 63.33333333 and deg <= 66.66666667:
        star="Mrigashirsha"
    elif deg > 66.66666667 and deg <= 70:
        star="Ardra"
    elif deg > 70 and deg <= 73.33333333:
        star="Ardra"
    elif deg > 73.33333333 and deg <= 76.66666667:
        star="Ardra"
    elif deg > 76.66666667 and deg <= 80:
        star="Ardra"
    elif deg > 80 and deg <= 83.33333333:
        star="Punarvasu"
    elif deg > 83.33333333 and deg <= 86.66666667:
        star="Punarvasu"
    elif deg > 86.66666667 and deg <= 90:
        star="Punarvasu"
    elif deg > 90 and deg <= 93.33333333:
        star="Punarvasu"
    elif deg > 93.33333333 and deg <= 96.66666667:
        star="Pushya"
    elif deg > 96.66666667 and deg <= 100:
        star="Pushya"
    elif deg > 100 and deg <= 103.3333333:
        star="Pushya"
    elif deg > 103.3333333 and deg <= 106.6666667:
        star="Pushya"
    elif deg > 106.6666667 and deg <= 110:
        star="Ashlesha"
    elif deg > 110 and deg <= 113.3333333:
        star="Ashlesha"
    elif deg > 113.3333333 and deg <= 116.6666667:
        star="Ashlesha"
    elif deg > 116.6666667 and deg <= 120:
        star="Ashlesha"
    elif deg > 120 and deg <= 123.3333333:
        star="Magha"
    elif deg > 123.3333333 and deg <= 126.6666667:
        star="Magha"
    elif deg > 126.6666667 and deg <= 130:
        star="Magha"
    elif deg > 130 and deg <= 133.3333333:
        star="Magha"
    elif deg > 133.3333333 and deg <= 136.6666667:
        star="Purva Phalguni"
    elif deg > 136.6666667 and deg <= 140:
        star="Purva Phalguni"
    elif deg > 140 and deg <= 143.3333333:
        star="Purva Phalguni"
    elif deg > 143.3333333 and deg <= 146.6666667:
        star="Purva Phalguni"
    elif deg > 146.6666667 and deg <= 150:
        star="Uttara Phalguni"
    elif deg > 150 and deg <= 153.3333333:
        star="Uttara Phalguni"
    elif deg > 153.3333333 and deg <= 156.6666667:
        star="Uttara Phalguni"
    elif deg > 156.6666667 and deg <= 160:
        star="Uttara Phalguni"
    elif deg > 160 and deg <= 163.3333333:
        star="Hasta"
    elif deg > 163.3333333 and deg <= 166.6666667:
        star="Hasta"
    elif deg > 166.6666667 and deg <= 170:
        star="Hasta"
    elif deg > 170 and deg <= 173.3333333:
        star="Hasta"
    elif deg > 173.3333333 and deg <= 176.6666667:
        star="Chitra"
    elif deg > 176.6666667 and deg <= 180:
        star="Chitra"
    elif deg > 180 and deg <= 183.3333333:
        star="Chitra"
    elif deg > 183.3333333 and deg <= 186.6666667:
        star="Chitra"
    elif deg > 186.6666667 and deg <= 190:
        star="Swati"
    elif deg > 190 and deg <= 193.3333333:
        star="Swati"
    elif deg > 193.3333333 and deg <= 196.6666667:
        star="Swati"
    elif deg > 196.6666667 and deg <= 200:
        star="Swati"
    elif deg > 200 and deg <= 203.3333333:
        star="Vishakha"
    elif deg > 203.3333333 and deg <= 206.6666667:
        star="Vishakha"
    elif deg > 206.6666667 and deg <= 210:
        star="Vishakha"
    elif deg > 210 and deg <= 213.3333333:
        star="Vishakha"
    elif deg > 213.3333333 and deg <= 216.6666667:
        star="Anuradha"
    elif deg > 216.6666667 and deg <= 220:
        star="Anuradha"
    elif deg > 220 and deg <= 223.3333333:
        star="Anuradha"
    elif deg > 223.3333333 and deg <= 226.6666667:
        star="Anuradha"
    elif deg > 226.6666667 and deg <= 230:
        star="Jyeshtha"
    elif deg > 230 and deg <= 233.3333333:
        star="Jyeshtha"
    elif deg > 233.3333333 and deg <= 236.6666667:
        star="Jyeshtha"
    elif deg > 236.6666667 and deg <= 240:
        star="Jyeshtha"
    elif deg > 240 and deg <= 243.3333333:
        star="Mula"
    elif deg > 243.3333333 and deg <= 246.6666667:
        star="Mula"
    elif deg > 246.6666667 and deg <= 250:
        star="Mula"
    elif deg > 250 and deg <= 253.3333333:
        star="Mula"
    elif deg > 253.3333333 and deg <= 256.6666667:
        star="Purva Ashadha"
    elif deg > 256.6666667 and deg <= 260:
        star="Purva Ashadha"
    elif deg > 260 and deg <= 263.3333333:
        star="Purva Ashadha"
    elif deg > 263.3333333 and deg <= 266.6666667:
        star="Purva Ashadha"
    elif deg > 266.6666667 and deg <= 270:
        star="Uttara Ashadha"
    elif deg > 270 and deg <= 273.3333333:
        star="Uttara Ashadha"
    elif deg > 273.3333333 and deg <= 276.6666667:
        star="Uttara Ashadha"
    elif deg > 276.6666667 and deg <= 280:
        star="Uttara Ashadha"
    elif deg > 280 and deg <= 283.3333333:
        star="Shravana"
    elif deg > 283.3333333 and deg <= 286.6666667:
        star="Shravana"
    elif deg > 286.6666667 and deg <= 290:
        star="Shravana"
    elif deg > 290 and deg <= 293.3333333:
        star="Shravana"
    elif deg > 23.3333333 and deg <= 296.6666667:
        star="Dhanishtha"
    elif deg > 296.6666667 and deg <= 300:
        star="Dhanishtha"
    elif deg > 300 and deg <= 303.3333333:
        star="Dhanishtha"
    elif deg > 303.3333333 and deg <= 306.6666667:
        star="Dhanishtha"
    elif deg > 306.6666667 and deg <= 310:
        star="Shatabhisha"
    elif deg > 310 and deg <= 313.3333333:
        star="Shatabhisha"
    elif deg > 313.3333333 and deg <= 316.6666667:
        star="Shatabhisha"
    elif deg > 316.6666667 and deg <= 320:
        star="Shatabhisha"
    elif deg > 320 and deg <= 323.3333333:
        star="Purva Bhadrapada"
    elif deg > 323.3333333 and deg <= 326.6666667:
        star="Purva Bhadrapada"
    elif deg > 326.6666667 and deg <= 330:
        star="Purva Bhadrapada"
    elif deg > 330 and deg <= 333.3333333:
        star="Purva Bhadrapada"
    elif deg > 333.3333333 and deg <= 336.6666667:
        star="Uttara Bhadrapada"
    elif deg > 336.6666667 and deg <= 340:
        star="Uttara Bhadrapada"
    elif deg > 340 and deg <= 343.3333333:
        star="Uttara Bhadrapada"
    elif deg > 343.3333333 and deg <= 346.6666667:
        star="Uttara Bhadrapada"
    elif deg > 346.6666667 and deg <= 350:
        star="Revati"
    elif deg > 350 and deg <= 353.3333333:
        star="Revati"
    elif deg > 353.3333333 and deg <= 356.6666667:
        star="Revati"
    elif deg > 356.6666667 and deg <= 360:
        star="Revati"
    
    return star
    
    
def star_padam(deg):
    if deg > 0 and deg <= 3.333333333:
        star="1"
    elif deg > 3.333333333 and deg <= 6.666666667:
        star="2"
    elif deg > 6.666666667 and deg <= 10:
        star="3"
    elif deg > 10 and deg <= 13.33333333:
        star="4"
    elif deg > 13.33333333 and deg <= 16.66666667:
        star="1"
    elif deg > 16.66666667 and deg <= 20:
        star="2"
    elif deg > 20 and deg <= 23.33333333:
        star="3"
    elif deg > 23.33333333 and deg <= 26.66666667:
        star="4"
    elif deg > 26.66666667 and deg <= 30:
        star="1"
    elif deg > 30 and deg <= 33.33333333:
        star="2"
    elif deg > 33.33333333 and deg <= 36.66666667:
        star="3"
    elif deg > 36.66666667 and deg <= 40:
        star="4"
    elif deg > 40 and deg <= 43.33333333:
        star="1"
    elif deg > 43.33333333 and deg <= 46.66666667:
        star="2"
    elif deg > 46.66666667 and deg <= 50:
        star="3"
    elif deg > 50 and deg <= 53.33333333:
        star="4"
    elif deg > 53.33333333 and deg <= 56.66666667:
        star="1"
    elif deg > 56.66666667 and deg <= 60:
        star="2"
    elif deg > 60 and deg <= 63.33333333:
        star="3"
    elif deg > 63.33333333 and deg <= 66.66666667:
        star="4"
    elif deg > 66.66666667 and deg <= 70:
        star="1"
    elif deg > 70 and deg <= 73.33333333:
        star="2"
    elif deg > 73.33333333 and deg <= 76.66666667:
        star="3"
    elif deg > 76.66666667 and deg <= 80:
        star="4"
    elif deg > 80 and deg <= 83.33333333:
        star="1"
    elif deg > 83.33333333 and deg <= 86.66666667:
        star="2"
    elif deg > 86.66666667 and deg <= 90:
        star="3"
    elif deg > 90 and deg <= 93.33333333:
        star="4"
    elif deg > 93.33333333 and deg <= 96.66666667:
        star="1"
    elif deg > 96.66666667 and deg <= 100:
        star="2"
    elif deg > 100 and deg <= 103.3333333:
        star="3"
    elif deg > 103.3333333 and deg <= 106.6666667:
        star="4"
    elif deg > 106.6666667 and deg <= 110:
        star="1"
    elif deg > 110 and deg <= 113.3333333:
        star="2"
    elif deg > 113.3333333 and deg <= 116.6666667:
        star="3"
    elif deg > 116.6666667 and deg <= 120:
        star="4"
    elif deg > 120 and deg <= 123.3333333:
        star="1"
    elif deg > 123.3333333 and deg <= 126.6666667:
        star="2"
    elif deg > 126.6666667 and deg <= 130:
        star="3"
    elif deg > 130 and deg <= 133.3333333:
        star="4"
    elif deg > 133.3333333 and deg <= 136.6666667:
        star="1"
    elif deg > 136.6666667 and deg <= 140:
        star="2"
    elif deg > 140 and deg <= 143.3333333:
        star="3"
    elif deg > 143.3333333 and deg <= 146.6666667:
        star="4"
    elif deg > 146.6666667 and deg <= 150:
        star="1"
    elif deg > 150 and deg <= 153.3333333:
        star="2"
    elif deg > 153.3333333 and deg <= 156.6666667:
        star="3"
    elif deg > 156.6666667 and deg <= 160:
        star="4"
    elif deg > 160 and deg <= 163.3333333:
        star="1"
    elif deg > 163.3333333 and deg <= 166.6666667:
        star="2"
    elif deg > 166.6666667 and deg <= 170:
        star="3"
    elif deg > 170 and deg <= 173.3333333:
        star="4"
    elif deg > 173.3333333 and deg <= 176.6666667:
        star="1"
    elif deg > 176.6666667 and deg <= 180:
        star="2"
    elif deg > 180 and deg <= 183.3333333:
        star="3"
    elif deg > 183.3333333 and deg <= 186.6666667:
        star="4"
    elif deg > 186.6666667 and deg <= 190:
        star="1"
    elif deg > 190 and deg <= 193.3333333:
        star="2"
    elif deg > 193.3333333 and deg <= 196.6666667:
        star="3"
    elif deg > 196.6666667 and deg <= 200:
        star="4"
    elif deg > 200 and deg <= 203.3333333:
        star="1"
    elif deg > 203.3333333 and deg <= 206.6666667:
        star="2"
    elif deg > 206.6666667 and deg <= 210:
        star="3"
    elif deg > 210 and deg <= 213.3333333:
        star="4"
    elif deg > 213.3333333 and deg <= 216.6666667:
        star="1"
    elif deg > 216.6666667 and deg <= 220:
        star="2"
    elif deg > 220 and deg <= 223.3333333:
        star="3"
    elif deg > 223.3333333 and deg <= 226.6666667:
        star="4"
    elif deg > 226.6666667 and deg <= 230:
        star="1"
    elif deg > 230 and deg <= 233.3333333:
        star="2"
    elif deg > 233.3333333 and deg <= 236.6666667:
        star="3"
    elif deg > 236.6666667 and deg <= 240:
        star="4"
    elif deg > 240 and deg <= 243.3333333:
        star="1"
    elif deg > 243.3333333 and deg <= 246.6666667:
        star="2"
    elif deg > 246.6666667 and deg <= 250:
        star="3"
    elif deg > 250 and deg <= 253.3333333:
        star="4"
    elif deg > 253.3333333 and deg <= 256.6666667:
        star="1"
    elif deg > 256.6666667 and deg <= 260:
        star="2"
    elif deg > 260 and deg <= 263.3333333:
        star="3"
    elif deg > 263.3333333 and deg <= 266.6666667:
        star="4"
    elif deg > 266.6666667 and deg <= 270:
        star="1"
    elif deg > 270 and deg <= 273.3333333:
        star="2"
    elif deg > 273.3333333 and deg <= 276.6666667:
        star="3"
    elif deg > 276.6666667 and deg <= 280:
        star="4"
    elif deg > 280 and deg <= 283.3333333:
        star="1"
    elif deg > 283.3333333 and deg <= 286.6666667:
        star="2"
    elif deg > 286.6666667 and deg <= 290:
        star="3"
    elif deg > 290 and deg <= 293.3333333:
        star="4"
    elif deg > 23.3333333 and deg <= 296.6666667:
        star="1"
    elif deg > 296.6666667 and deg <= 300:
        star="2"
    elif deg > 300 and deg <= 303.3333333:
        star="3"
    elif deg > 303.3333333 and deg <= 306.6666667:
        star="4"
    elif deg > 306.6666667 and deg <= 310:
        star="1"
    elif deg > 310 and deg <= 313.3333333:
        star="2"
    elif deg > 313.3333333 and deg <= 316.6666667:
        star="3"
    elif deg > 316.6666667 and deg <= 320:
        star="4"
    elif deg > 320 and deg <= 323.3333333:
        star="1"
    elif deg > 323.3333333 and deg <= 326.6666667:
        star="2"
    elif deg > 326.6666667 and deg <= 330:
        star="3"
    elif deg > 330 and deg <= 333.3333333:
        star="4"
    elif deg > 333.3333333 and deg <= 336.6666667:
        star="1"
    elif deg > 336.6666667 and deg <= 340:
        star="2"
    elif deg > 340 and deg <= 343.3333333:
        star="3"
    elif deg > 343.3333333 and deg <= 346.6666667:
        star="4"
    elif deg > 346.6666667 and deg <= 350:
        star="1"
    elif deg > 350 and deg <= 353.3333333:
        star="2"
    elif deg > 353.3333333 and deg <= 356.6666667:
        star="3"
    elif deg > 356.6666667 and deg <= 360:
        star="4"
    
    return star    
    
def star_lord(deg):
    if deg > 0 and deg <= 3.333333333:
        star="Kethu"
    elif deg > 3.333333333 and deg <= 6.666666667:
        star="Kethu"
    elif deg > 6.666666667 and deg <= 10:
        star="Kethu"
    elif deg > 10 and deg <= 13.33333333:
        star="Kethu"
    elif deg > 13.33333333 and deg <= 16.66666667:
        star="Venus"
    elif deg > 16.66666667 and deg <= 20:
        star="Venus"
    elif deg > 20 and deg <= 23.33333333:
        star="Venus"
    elif deg > 23.33333333 and deg <= 26.66666667:
        star="Venus"
    elif deg > 26.66666667 and deg <= 30:
        star="Sun"
    elif deg > 30 and deg <= 33.33333333:
        star="Sun"
    elif deg > 33.33333333 and deg <= 36.66666667:
        star="Sun"
    elif deg > 36.66666667 and deg <= 40:
        star="Sun"
    elif deg > 40 and deg <= 43.33333333:
        star="Moon"
    elif deg > 43.33333333 and deg <= 46.66666667:
        star="Moon"
    elif deg > 46.66666667 and deg <= 50:
        star="Moon"
    elif deg > 50 and deg <= 53.33333333:
        star="Moon"
    elif deg > 53.33333333 and deg <= 56.66666667:
        star="Mars"
    elif deg > 56.66666667 and deg <= 60:
        star="Mars"
    elif deg > 60 and deg <= 63.33333333:
        star="Mars"
    elif deg > 63.33333333 and deg <= 66.66666667:
        star="Mars"
    elif deg > 66.66666667 and deg <= 70:
        star="Raghu"
    elif deg > 70 and deg <= 73.33333333:
        star="Raghu"
    elif deg > 73.33333333 and deg <= 76.66666667:
        star="Raghu"
    elif deg > 76.66666667 and deg <= 80:
        star="Raghu"
    elif deg > 80 and deg <= 83.33333333:
        star="Jupiter"
    elif deg > 83.33333333 and deg <= 86.66666667:
        star="Jupiter"
    elif deg > 86.66666667 and deg <= 90:
        star="Jupiter"
    elif deg > 90 and deg <= 93.33333333:
        star="Jupiter"
    elif deg > 93.33333333 and deg <= 96.66666667:
        star="Saturn"
    elif deg > 96.66666667 and deg <= 100:
        star="Saturn"
    elif deg > 100 and deg <= 103.3333333:
        star="Saturn"
    elif deg > 103.3333333 and deg <= 106.6666667:
        star="Saturn"
    elif deg > 106.6666667 and deg <= 110:
        star="Mercury"
    elif deg > 110 and deg <= 113.3333333:
        star="Mercury"
    elif deg > 113.3333333 and deg <= 116.6666667:
        star="Mercury"
    elif deg > 116.6666667 and deg <= 120:
        star="Mercury"
    elif deg > 120 and deg <= 123.3333333:
        star="Kethu"
    elif deg > 123.3333333 and deg <= 126.6666667:
        star="Kethu"
    elif deg > 126.6666667 and deg <= 130:
        star="Kethu"
    elif deg > 130 and deg <= 133.3333333:
        star="Kethu"
    elif deg > 133.3333333 and deg <= 136.6666667:
        star="Venus"
    elif deg > 136.6666667 and deg <= 140:
        star="Venus"
    elif deg > 140 and deg <= 143.3333333:
        star="Venus"
    elif deg > 143.3333333 and deg <= 146.6666667:
        star="Venus"
    elif deg > 146.6666667 and deg <= 150:
        star="Sun"
    elif deg > 150 and deg <= 153.3333333:
        star="Sun"
    elif deg > 153.3333333 and deg <= 156.6666667:
        star="Sun"
    elif deg > 156.6666667 and deg <= 160:
        star="Sun"
    elif deg > 160 and deg <= 163.3333333:
        star="Moon"
    elif deg > 163.3333333 and deg <= 166.6666667:
        star="Moon"
    elif deg > 166.6666667 and deg <= 170:
        star="Moon"
    elif deg > 170 and deg <= 173.3333333:
        star="Moon"
    elif deg > 173.3333333 and deg <= 176.6666667:
        star="Mars"
    elif deg > 176.6666667 and deg <= 180:
        star="Mars"
    elif deg > 180 and deg <= 183.3333333:
        star="Mars"
    elif deg > 183.3333333 and deg <= 186.6666667:
        star="Mars"
    elif deg > 186.6666667 and deg <= 190:
        star="Raghu"
    elif deg > 190 and deg <= 193.3333333:
        star="Raghu"
    elif deg > 193.3333333 and deg <= 196.6666667:
        star="Raghu"
    elif deg > 196.6666667 and deg <= 200:
        star="Raghu"
    elif deg > 200 and deg <= 203.3333333:
        star="Jupiter"
    elif deg > 203.3333333 and deg <= 206.6666667:
        star="Jupiter"
    elif deg > 206.6666667 and deg <= 210:
        star="Jupiter"
    elif deg > 210 and deg <= 213.3333333:
        star="Jupiter"
    elif deg > 213.3333333 and deg <= 216.6666667:
        star="Saturn"
    elif deg > 216.6666667 and deg <= 220:
        star="Saturn"
    elif deg > 220 and deg <= 223.3333333:
        star="Saturn"
    elif deg > 223.3333333 and deg <= 226.6666667:
        star="Saturn"
    elif deg > 226.6666667 and deg <= 230:
        star="Mercury"
    elif deg > 230 and deg <= 233.3333333:
        star="Mercury"
    elif deg > 233.3333333 and deg <= 236.6666667:
        star="Mercury"
    elif deg > 236.6666667 and deg <= 240:
        star="Mercury"
    elif deg > 240 and deg <= 243.3333333:
        star="Kethu"
    elif deg > 243.3333333 and deg <= 246.6666667:
        star="Kethu"
    elif deg > 246.6666667 and deg <= 250:
        star="Kethu"
    elif deg > 250 and deg <= 253.3333333:
        star="Kethu"
    elif deg > 253.3333333 and deg <= 256.6666667:
        star="Venus"
    elif deg > 256.6666667 and deg <= 260:
        star="Venus"
    elif deg > 260 and deg <= 263.3333333:
        star="Venus"
    elif deg > 263.3333333 and deg <= 266.6666667:
        star="Venus"
    elif deg > 266.6666667 and deg <= 270:
        star="Sun"
    elif deg > 270 and deg <= 273.3333333:
        star="Sun"
    elif deg > 273.3333333 and deg <= 276.6666667:
        star="Sun"
    elif deg > 276.6666667 and deg <= 280:
        star="Sun"
    elif deg > 280 and deg <= 283.3333333:
        star="Moon"
    elif deg > 283.3333333 and deg <= 286.6666667:
        star="Moon"
    elif deg > 286.6666667 and deg <= 290:
        star="Moon"
    elif deg > 290 and deg <= 293.3333333:
        star="Moon"
    elif deg > 23.3333333 and deg <= 296.6666667:
        star="Mars"
    elif deg > 296.6666667 and deg <= 300:
        star="Mars"
    elif deg > 300 and deg <= 303.3333333:
        star="Mars"
    elif deg > 303.3333333 and deg <= 306.6666667:
        star="Mars"
    elif deg > 306.6666667 and deg <= 310:
        star="Raghu"
    elif deg > 310 and deg <= 313.3333333:
        star="Raghu"
    elif deg > 313.3333333 and deg <= 316.6666667:
        star="Raghu"
    elif deg > 316.6666667 and deg <= 320:
        star="Raghu"
    elif deg > 320 and deg <= 323.3333333:
        star="Jupiter"
    elif deg > 323.3333333 and deg <= 326.6666667:
        star="Jupiter"
    elif deg > 326.6666667 and deg <= 330:
        star="Jupiter"
    elif deg > 330 and deg <= 333.3333333:
        star="Jupiter"
    elif deg > 333.3333333 and deg <= 336.6666667:
        star="Saturn"
    elif deg > 336.6666667 and deg <= 340:
        star="Saturn"
    elif deg > 340 and deg <= 343.3333333:
        star="Saturn"
    elif deg > 343.3333333 and deg <= 346.6666667:
        star="Saturn"
    elif deg > 346.6666667 and deg <= 350:
        star="Mercury"
    elif deg > 350 and deg <= 353.3333333:
        star="Mercury"
    elif deg > 353.3333333 and deg <= 356.6666667:
        star="Mercury"
    elif deg > 356.6666667 and deg <= 360:
        star="Mercury"
    
    return star
    
def star_lord_tamil(deg):
    if deg > 0 and deg <= 3.333333333:
        star="கேது"
    elif deg > 3.333333333 and deg <= 6.666666667:
        star="கேது"
    elif deg > 6.666666667 and deg <= 10:
        star="கேது"
    elif deg > 10 and deg <= 13.33333333:
        star="கேது"
    elif deg > 13.33333333 and deg <= 16.66666667:
        star="சுக்ரன்"
    elif deg > 16.66666667 and deg <= 20:
        star="சுக்ரன்"
    elif deg > 20 and deg <= 23.33333333:
        star="சுக்ரன்"
    elif deg > 23.33333333 and deg <= 26.66666667:
        star="சுக்ரன்"
    elif deg > 26.66666667 and deg <= 30:
        star="சூரியன்"
    elif deg > 30 and deg <= 33.33333333:
        star="சூரியன்"
    elif deg > 33.33333333 and deg <= 36.66666667:
        star="சூரியன்"
    elif deg > 36.66666667 and deg <= 40:
        star="சூரியன்"
    elif deg > 40 and deg <= 43.33333333:
        star="சந்திரன்"
    elif deg > 43.33333333 and deg <= 46.66666667:
        star="சந்திரன்"
    elif deg > 46.66666667 and deg <= 50:
        star="சந்திரன்"
    elif deg > 50 and deg <= 53.33333333:
        star="சந்திரன்"
    elif deg > 53.33333333 and deg <= 56.66666667:
        star="செவ்வாய்"
    elif deg > 56.66666667 and deg <= 60:
        star="செவ்வாய்"
    elif deg > 60 and deg <= 63.33333333:
        star="செவ்வாய்"
    elif deg > 63.33333333 and deg <= 66.66666667:
        star="செவ்வாய்"
    elif deg > 66.66666667 and deg <= 70:
        star="ராகு"
    elif deg > 70 and deg <= 73.33333333:
        star="ராகு"
    elif deg > 73.33333333 and deg <= 76.66666667:
        star="ராகு"
    elif deg > 76.66666667 and deg <= 80:
        star="ராகு"
    elif deg > 80 and deg <= 83.33333333:
        star="குரு"
    elif deg > 83.33333333 and deg <= 86.66666667:
        star="குரு"
    elif deg > 86.66666667 and deg <= 90:
        star="குரு"
    elif deg > 90 and deg <= 93.33333333:
        star="குரு"
    elif deg > 93.33333333 and deg <= 96.66666667:
        star="சனி"
    elif deg > 96.66666667 and deg <= 100:
        star="சனி"
    elif deg > 100 and deg <= 103.3333333:
        star="சனி"
    elif deg > 103.3333333 and deg <= 106.6666667:
        star="சனி"
    elif deg > 106.6666667 and deg <= 110:
        star="புதன்"
    elif deg > 110 and deg <= 113.3333333:
        star="புதன்"
    elif deg > 113.3333333 and deg <= 116.6666667:
        star="புதன்"
    elif deg > 116.6666667 and deg <= 120:
        star="புதன்"
    elif deg > 120 and deg <= 123.3333333:
        star="கேது"
    elif deg > 123.3333333 and deg <= 126.6666667:
        star="கேது"
    elif deg > 126.6666667 and deg <= 130:
        star="கேது"
    elif deg > 130 and deg <= 133.3333333:
        star="கேது"
    elif deg > 133.3333333 and deg <= 136.6666667:
        star="சுக்ரன்"
    elif deg > 136.6666667 and deg <= 140:
        star="சுக்ரன்"
    elif deg > 140 and deg <= 143.3333333:
        star="சுக்ரன்"
    elif deg > 143.3333333 and deg <= 146.6666667:
        star="சுக்ரன்"
    elif deg > 146.6666667 and deg <= 150:
        star="சூரியன்"
    elif deg > 150 and deg <= 153.3333333:
        star="சூரியன்"
    elif deg > 153.3333333 and deg <= 156.6666667:
        star="சூரியன்"
    elif deg > 156.6666667 and deg <= 160:
        star="சூரியன்"
    elif deg > 160 and deg <= 163.3333333:
        star="சந்திரன்"
    elif deg > 163.3333333 and deg <= 166.6666667:
        star="சந்திரன்"
    elif deg > 166.6666667 and deg <= 170:
        star="சந்திரன்"
    elif deg > 170 and deg <= 173.3333333:
        star="சந்திரன்"
    elif deg > 173.3333333 and deg <= 176.6666667:
        star="செவ்வாய்"
    elif deg > 176.6666667 and deg <= 180:
        star="செவ்வாய்"
    elif deg > 180 and deg <= 183.3333333:
        star="செவ்வாய்"
    elif deg > 183.3333333 and deg <= 186.6666667:
        star="செவ்வாய்"
    elif deg > 186.6666667 and deg <= 190:
        star="ராகு"
    elif deg > 190 and deg <= 193.3333333:
        star="ராகு"
    elif deg > 193.3333333 and deg <= 196.6666667:
        star="ராகு"
    elif deg > 196.6666667 and deg <= 200:
        star="ராகு"
    elif deg > 200 and deg <= 203.3333333:
        star="குரு"
    elif deg > 203.3333333 and deg <= 206.6666667:
        star="குரு"
    elif deg > 206.6666667 and deg <= 210:
        star="குரு"
    elif deg > 210 and deg <= 213.3333333:
        star="குரு"
    elif deg > 213.3333333 and deg <= 216.6666667:
        star="சனி"
    elif deg > 216.6666667 and deg <= 220:
        star="சனி"
    elif deg > 220 and deg <= 223.3333333:
        star="சனி"
    elif deg > 223.3333333 and deg <= 226.6666667:
        star="சனி"
    elif deg > 226.6666667 and deg <= 230:
        star="புதன்"
    elif deg > 230 and deg <= 233.3333333:
        star="புதன்"
    elif deg > 233.3333333 and deg <= 236.6666667:
        star="புதன்"
    elif deg > 236.6666667 and deg <= 240:
        star="புதன்"
    elif deg > 240 and deg <= 243.3333333:
        star="கேது"
    elif deg > 243.3333333 and deg <= 246.6666667:
        star="கேது"
    elif deg > 246.6666667 and deg <= 250:
        star="கேது"
    elif deg > 250 and deg <= 253.3333333:
        star="கேது"
    elif deg > 253.3333333 and deg <= 256.6666667:
        star="சுக்ரன்"
    elif deg > 256.6666667 and deg <= 260:
        star="சுக்ரன்"
    elif deg > 260 and deg <= 263.3333333:
        star="சுக்ரன்"
    elif deg > 263.3333333 and deg <= 266.6666667:
        star="சுக்ரன்"
    elif deg > 266.6666667 and deg <= 270:
        star="சூரியன்"
    elif deg > 270 and deg <= 273.3333333:
        star="சூரியன்"
    elif deg > 273.3333333 and deg <= 276.6666667:
        star="சூரியன்"
    elif deg > 276.6666667 and deg <= 280:
        star="சூரியன்"
    elif deg > 280 and deg <= 283.3333333:
        star="சந்திரன்"
    elif deg > 283.3333333 and deg <= 286.6666667:
        star="சந்திரன்"
    elif deg > 286.6666667 and deg <= 290:
        star="சந்திரன்"
    elif deg > 290 and deg <= 293.3333333:
        star="சந்திரன்"
    elif deg > 23.3333333 and deg <= 296.6666667:
        star="செவ்வாய்"
    elif deg > 296.6666667 and deg <= 300:
        star="செவ்வாய்"
    elif deg > 300 and deg <= 303.3333333:
        star="செவ்வாய்"
    elif deg > 303.3333333 and deg <= 306.6666667:
        star="செவ்வாய்"
    elif deg > 306.6666667 and deg <= 310:
        star="ராகு"
    elif deg > 310 and deg <= 313.3333333:
        star="ராகு"
    elif deg > 313.3333333 and deg <= 316.6666667:
        star="ராகு"
    elif deg > 316.6666667 and deg <= 320:
        star="ராகு"
    elif deg > 320 and deg <= 323.3333333:
        star="குரு"
    elif deg > 323.3333333 and deg <= 326.6666667:
        star="குரு"
    elif deg > 326.6666667 and deg <= 330:
        star="குரு"
    elif deg > 330 and deg <= 333.3333333:
        star="குரு"
    elif deg > 333.3333333 and deg <= 336.6666667:
        star="சனி"
    elif deg > 336.6666667 and deg <= 340:
        star="சனி"
    elif deg > 340 and deg <= 343.3333333:
        star="சனி"
    elif deg > 343.3333333 and deg <= 346.6666667:
        star="சனி"
    elif deg > 346.6666667 and deg <= 350:
        star="புதன்"
    elif deg > 350 and deg <= 353.3333333:
        star="புதன்"
    elif deg > 353.3333333 and deg <= 356.6666667:
        star="புதன்"
    elif deg > 356.6666667 and deg <= 360:
        star="புதன்"
    
    return star    
    
    
def amsamrasi(deg):
    if deg > 0 and deg <= 3.333333333:
        star="MESHAM"
    elif deg > 3.333333333 and deg <= 6.666666667:
        star="RISHABAM"
    elif deg > 6.666666667 and deg <= 10:
        star="MITHUNAM"
    elif deg > 10 and deg <= 13.33333333:
        star="KADAGAM"
    elif deg > 13.33333333 and deg <= 16.66666667:
        star="SIMMAM"
    elif deg > 16.66666667 and deg <= 20:
        star="KANNI"
    elif deg > 20 and deg <= 23.33333333:
        star="THULAM"
    elif deg > 23.33333333 and deg <= 26.66666667:
        star="VIRUCHIGAM"
    elif deg > 26.66666667 and deg <= 30:
        star="DHANUSU"
    elif deg > 30 and deg <= 33.33333333:
        star="MAGARAM"
    elif deg > 33.33333333 and deg <= 36.66666667:
        star="KUMBAM"
    elif deg > 36.66666667 and deg <= 40:
        star="MEENAM"
    elif deg > 40 and deg <= 43.33333333:
        star="MESHAM"
    elif deg > 43.33333333 and deg <= 46.66666667:
        star="RISHABAM"
    elif deg > 46.66666667 and deg <= 50:
        star="MITHUNAM"
    elif deg > 50 and deg <= 53.33333333:
        star="KADAGAM"
    elif deg > 53.33333333 and deg <= 56.66666667:
        star="SIMMAM"
    elif deg > 56.66666667 and deg <= 60:
        star="KANNI"
    elif deg > 60 and deg <= 63.33333333:
        star="THULAM"
    elif deg > 63.33333333 and deg <= 66.66666667:
        star="VIRUCHIGAM"
    elif deg > 66.66666667 and deg <= 70:
        star="DHANUSU"
    elif deg > 70 and deg <= 73.33333333:
        star="MAGARAM"
    elif deg > 73.33333333 and deg <= 76.66666667:
        star="KUMBAM"
    elif deg > 76.66666667 and deg <= 80:
        star="MEENAM"
    elif deg > 80 and deg <= 83.33333333:
        star="MESHAM"
    elif deg > 83.33333333 and deg <= 86.66666667:
        star="RISHABAM"
    elif deg > 86.66666667 and deg <= 90:
        star="MITHUNAM"
    elif deg > 90 and deg <= 93.33333333:
        star="KADAGAM"
    elif deg > 93.33333333 and deg <= 96.66666667:
        star="SIMMAM"
    elif deg > 96.66666667 and deg <= 100:
        star="KANNI"
    elif deg > 100 and deg <= 103.3333333:
        star="THULAM"
    elif deg > 103.3333333 and deg <= 106.6666667:
        star="VIRUCHIGAM"
    elif deg > 106.6666667 and deg <= 110:
        star="DHANUSU"
    elif deg > 110 and deg <= 113.3333333:
        star="MAGARAM"
    elif deg > 113.3333333 and deg <= 116.6666667:
        star="KUMBAM"
    elif deg > 116.6666667 and deg <= 120:
        star="MEENAM"
    elif deg > 120 and deg <= 123.3333333:
        star="MESHAM"
    elif deg > 123.3333333 and deg <= 126.6666667:
        star="RISHABAM"
    elif deg > 126.6666667 and deg <= 130:
        star="MITHUNAM"
    elif deg > 130 and deg <= 133.3333333:
        star="KADAGAM"
    elif deg > 133.3333333 and deg <= 136.6666667:
        star="SIMMAM"
    elif deg > 136.6666667 and deg <= 140:
        star="KANNI"
    elif deg > 140 and deg <= 143.3333333:
        star="THULAM"
    elif deg > 143.3333333 and deg <= 146.6666667:
        star="VIRUCHIGAM"
    elif deg > 146.6666667 and deg <= 150:
        star="DHANUSU"
    elif deg > 150 and deg <= 153.3333333:
        star="MAGARAM"
    elif deg > 153.3333333 and deg <= 156.6666667:
        star="KUMBAM"
    elif deg > 156.6666667 and deg <= 160:
        star="MEENAM"
    elif deg > 160 and deg <= 163.3333333:
        star="MESHAM"
    elif deg > 163.3333333 and deg <= 166.6666667:
        star="RISHABAM"
    elif deg > 166.6666667 and deg <= 170:
        star="MITHUNAM"
    elif deg > 170 and deg <= 173.3333333:
        star="KADAGAM"
    elif deg > 173.3333333 and deg <= 176.6666667:
        star="SIMMAM"
    elif deg > 176.6666667 and deg <= 180:
        star="KANNI"
    elif deg > 180 and deg <= 183.3333333:
        star="THULAM"
    elif deg > 183.3333333 and deg <= 186.6666667:
        star="VIRUCHIGAM"
    elif deg > 186.6666667 and deg <= 190:
        star="DHANUSU"
    elif deg > 190 and deg <= 193.3333333:
        star="MAGARAM"
    elif deg > 193.3333333 and deg <= 196.6666667:
        star="KUMBAM"
    elif deg > 196.6666667 and deg <= 200:
        star="MEENAM"
    elif deg > 200 and deg <= 203.3333333:
        star="MESHAM"
    elif deg > 203.3333333 and deg <= 206.6666667:
        star="RISHABAM"
    elif deg > 206.6666667 and deg <= 210:
        star="MITHUNAM"
    elif deg > 210 and deg <= 213.3333333:
        star="KADAGAM"
    elif deg > 213.3333333 and deg <= 216.6666667:
        star="SIMMAM"
    elif deg > 216.6666667 and deg <= 220:
        star="KANNI"
    elif deg > 220 and deg <= 223.3333333:
        star="THULAM"
    elif deg > 223.3333333 and deg <= 226.6666667:
        star="VIRUCHIGAM"
    elif deg > 226.6666667 and deg <= 230:
        star="DHANUSU"
    elif deg > 230 and deg <= 233.3333333:
        star="MAGARAM"
    elif deg > 233.3333333 and deg <= 236.6666667:
        star="KUMBAM"
    elif deg > 236.6666667 and deg <= 240:
        star="MEENAM"
    elif deg > 240 and deg <= 243.3333333:
        star="MESHAM"
    elif deg > 243.3333333 and deg <= 246.6666667:
        star="RISHABAM"
    elif deg > 246.6666667 and deg <= 250:
        star="MITHUNAM"
    elif deg > 250 and deg <= 253.3333333:
        star="KADAGAM"
    elif deg > 253.3333333 and deg <= 256.6666667:
        star="SIMMAM"
    elif deg > 256.6666667 and deg <= 260:
        star="KANNI"
    elif deg > 260 and deg <= 263.3333333:
        star="THULAM"
    elif deg > 263.3333333 and deg <= 266.6666667:
        star="VIRUCHIGAM"
    elif deg > 266.6666667 and deg <= 270:
        star="DHANUSU"
    elif deg > 270 and deg <= 273.3333333:
        star="MAGARAM"
    elif deg > 273.3333333 and deg <= 276.6666667:
        star="KUMBAM"
    elif deg > 276.6666667 and deg <= 280:
        star="MEENAM"
    elif deg > 280 and deg <= 283.3333333:
        star="MESHAM"
    elif deg > 283.3333333 and deg <= 286.6666667:
        star="RISHABAM"
    elif deg > 286.6666667 and deg <= 290:
        star="MITHUNAM"
    elif deg > 290 and deg <= 293.3333333:
        star="KADAGAM"
    elif deg > 23.3333333 and deg <= 296.6666667:
        star="SIMMAM"
    elif deg > 296.6666667 and deg <= 300:
        star="KANNI"
    elif deg > 300 and deg <= 303.3333333:
        star="THULAM"
    elif deg > 303.3333333 and deg <= 306.6666667:
        star="VIRUCHIGAM"
    elif deg > 306.6666667 and deg <= 310:
        star="DHANUSU"
    elif deg > 310 and deg <= 313.3333333:
        star="MAGARAM"
    elif deg > 313.3333333 and deg <= 316.6666667:
        star="KUMBAM"
    elif deg > 316.6666667 and deg <= 320:
        star="MEENAM"
    elif deg > 320 and deg <= 323.3333333:
        star="MESHAM"
    elif deg > 323.3333333 and deg <= 326.6666667:
        star="RISHABAM"
    elif deg > 326.6666667 and deg <= 330:
        star="MITHUNAM"
    elif deg > 330 and deg <= 333.3333333:
        star="KADAGAM"
    elif deg > 333.3333333 and deg <= 336.6666667:
        star="SIMMAM"
    elif deg > 336.6666667 and deg <= 340:
        star="KANNI"
    elif deg > 340 and deg <= 343.3333333:
        star="THULAM"
    elif deg > 343.3333333 and deg <= 346.6666667:
        star="VIRUCHIGAM"
    elif deg > 346.6666667 and deg <= 350:
        star="DHANUSU"
    elif deg > 350 and deg <= 353.3333333:
        star="MAGARAM"
    elif deg > 353.3333333 and deg <= 356.6666667:
        star="KUMBAM"
    elif deg > 356.6666667 and deg <= 360:
        star="MEENAM"
    
    return star        
#print(get_planet_house(125.3583169))
#print(get_planet_degree(125.3583169))
#print(Convert_Longitude_into_time(125.3583169))
#print(star_query(125.3583169))
#print(star_lord(125.3583169))

def p_format(s):
    cnt=0
    str1 = ""  
    for ele in s:  
        str1 += ele 
        cnt=cnt+1
        if cnt==2:
            cnt=0
            str1 += "<br>"
        else:
            str1 += " "

    return str1
    
def p1_format(s):
    cnt=0
    lin=0
    str1 = ""  
    for ele in s:  
        str1 += ele 
        cnt=cnt+1
        lin=lin+1
        if cnt==2:
            cnt=0
            str1 += "\n"
        elif cnt==1:
            str1 += " "

    if lin==0:
        str1=str1 + "\n\n\n"    
    elif lin==1:
        str1=str1 + "\n\n\n"
    elif lin==2:    
        str1=str1 + "\n"
    elif lin==3:    
        str1=str1 + "\n"

        
    return str1
    
def find_thithi(moonlat, sunlat, language):
    thithi = ["0","Shukla Paksha Prathama", "Shukla Paksha Dwitiya", "Shukla Paksha Tritiya", "Shukla Paksha Chaturthi", "Shukla Paksha Panchami", "Shukla Paksha Shashthi", "Shukla Paksha Saptami", "Shukla Paksha Ashtami", "Shukla Paksha Navami", "Shukla Paksha Dashami", "Shukla Paksha Ekadashi", "Shukla Paksha Dwadashi","Shukla Paksha Thrayodashi","Shukla Paksha Chaturdashi","Purnima","Krishna Paksha Prathama", "Krishna Paksha Dwitiya", "Krishna Paksha Tritiya", "Krishna Paksha Chaturthi", "Krishna Paksha Panchami", "Krishna Paksha Shashthi", "Krishna Paksha Saptami", "Krishna Paksha Ashtami", "Krishna Paksha Navami", "Krishna Paksha Dashami", "Krishna Paksha Ekadashi", "Krishna Paksha Dwadashi","Krishna Paksha Thrayodashi","Krishna Paksha Chaturdashi","Amavasya"]

    
    #thithi_tamil = ["0","சுக்லபட்சம் பிரதமை","சுக்லபட்சம் த்விதியை","சுக்லபட்சம் த்ரிதியை","சுக்லபட்சம் சதுர்த்தி","சுக்லபட்சம் பஞ்ஜமி","சுக்லபட்சம் சஷ்டி","சுக்லபட்சம் சப்தமி","சுக்லபட்சம் அஷ்டமி","சுக்லபட்சம் நவமி","சுக்லபட்சம் தசமி","சுக்லபட்சம் ஏகாதசி","சுக்லபட்சம் த்வாதசி","சுக்லபட்சம் த்ரயோதசி","சுக்லபட்சம் சதுர்தசி","பொளர்ணமி","கிருஷ்ணபட்சம் பிரதமை","கிருஷ்ணபட்சம் த்விதியை","கிருஷ்ணபட்சம் த்ரிதியை","கிருஷ்ணபட்சம் சதுர்த்தி","கிருஷ்ணபட்சம் பஞ்ஜமி","கிருஷ்ணபட்சம் சஷ்டி","கிருஷ்ணபட்சம் சப்தமி","கிருஷ்ணபட்சம் அஷ்டமி","கிருஷ்ணபட்சம் நவமி","கிருஷ்ணபட்சம் தசமி","கிருஷ்ணபட்சம் ஏகாதசி","கிருஷ்ணபட்சம் த்வாதசி","கிருஷ்ணபட்சம் த்ரயோதசி","கிருஷ்ணபட்சம் சதுர்தசி","அமாவாசை"]

    thithi_tamil = ["0","சுக்ல. பிரதமை","சுக்ல. த்விதியை","சுக்ல. த்ரிதியை","சுக்ல. சதுர்த்தி","சுக்ல. பஞ்ஜமி","சுக்ல. சஷ்டி","சுக்ல. சப்தமி","சுக்ல. அஷ்டமி","சுக்ல. நவமி","சுக்ல. தசமி","சுக்ல. ஏகாதசி","சுக்ல. த்வாதசி","சுக்ல. த்ரயோதசி","சுக்ல. சதுர்தசி","பொளர்ணமி","கிருஷ்ண. பிரதமை","கிருஷ்ண.  த்விதியை","கிருஷ்ண.  த்ரிதியை","கிருஷ்ண.  சதுர்த்தி","கிருஷ்ண.  பஞ்ஜமி","கிருஷ்ண.  சஷ்டி","கிருஷ்ண.  சப்தமி","கிருஷ்ண.  அஷ்டமி","கிருஷ்ண.  நவமி","கிருஷ்ண.  தசமி","கிருஷ்ண.  ஏகாதசி","கிருஷ்ண.  த்வாதசி","கிருஷ்ண.  த்ரயோதசி","கிருஷ்ண.  சதுர்தசி","அமாவாசை"]
    
    diffmoonsunlat = float(moonlat) - float(sunlat)

    if diffmoonsunlat < 0:
        thitinumber = math.ceil((diffmoonsunlat + 360) / 12)
    else:
        thitinumber = math.ceil((diffmoonsunlat) / 12)
        
    if language=="english":
        return thithi[thitinumber]
    elif language=="tamil":
        return thithi_tamil[thitinumber]    


def find_yoga(moonlat, sunlat, language):    
    nithiyayoga = ["0","Vishkumbh yoga","Preeti Yoga","Ayushman Yoga","Saubhagya Yoga","Shobhan Yoga","Atigand Yoga","Sukarma yoga","Dhriti Yoga","Shool yoga","Gand Yoga","Vridhhi yoga","Dhruva Yoga","Vyaghat Yoga","Harshan Yoga","Vajra Yoga","Siddha Yoga","Vyatipat Yoga","Variyan Yoga","Paridh Yoga","Shiva Yoga","Siddha Yoga","Sadhya Yoga","Shubh Yoga","Shukla Yoga","Brahma Yoga","Aindra Yoga","Vaidhriti Yoga"]


    nithiyayogatamil = ["0","விஷ்கம்பம்","பரீதி","ஆயுஸ்மான்","சௌபாக்கியம்","சோபனம்","அதிகண்டம்","சகர்மம்","திரிதி","சூலம்","கண்டம்","விருத்தி","த்ருவம்","வியகாதம்","ஹர்ஷணம்","வச்சிரம்","கித்தி","விதிபாதம்","வரியான்","பரிகம்","சிவம்","சித்தம்","ஸாயம்","சுபம்","சுப்ரம்","பிரமம்","மகேந்திரம்","வைகிருதி"]

    temp = float(moonlat) + float(sunlat)

    if temp > 360:
        temp = temp - 360
 

    t2 = temp / 13.333333333333334

    yoga = t2 + 1


    if language=="english":
        return nithiyayoga[math.floor(yoga)]
    elif language=="tamil":
        return nithiyayogatamil[math.floor(yoga)]

        

def find_karnam(moonlat, sunlat, language):
    
    thithi_first = ["0","Kimstugna","Balava","Taitila","Vanija","Bava","Kaulava","Gara","Vishti","Balava","Taitila","Vanija","Bava","Kaulava","Gara","Vishti","Balava","Taitila","Vanija","Bava","Kaulava","Gara","Vishti","Balava","Taitila","Vanija","Bava","Kaulava","Gara","Vishti","Chatushpada"]


    thithi_second = ["0","Bava","Kaulava","Gara","Vishti","Balava","Taitila","Vanija","Bava","Kaulava","Gara","Vishti","Balava","Taitila","Vanija","Bava","Kaulava","Gara","Vishti","Balava","Taitila","Vanija","Bava","Kaulava","Gara","Vishti","Balava","Taitila","Vanija","Shakuni","Naga"]


    thithi_first_tamil = ["0","கிம்ஸ்துக்னம்","பாலவ","தைதூலை","வணிசை","பவ","கௌலவ","கரசை","பத்தரை","பாலவ","தைதூலை","வணிசை","பவ","கௌலவ","கரசை","பத்தரை","பாலவ","தைதூலை","வணிசை","பவ","கௌலவ","கரசை","பத்தரை","பாலவ","தைதூலை","வணிசை","பவ","கௌலவ","கரசை","பத்தரை","சதுஷ்பாதம்"]

    
    thithi_second_tamil = ["0","பவ","கௌலவ","கரசை","பத்தரை","பாலவ","தைதூலை","வணிசை","பவ","கௌலவ","கரசை","பத்தரை","பாலவ","தைதூலை","வணிசை","பவ","கௌலவ","கரசை","பத்தரை","பாலவ","தைதூலை","வணிசை","பவ","கௌலவ","கரசை","பத்தரை","பாலவ","தைதூலை","வணிசை","சகுனி","நாகவம்"]


    diffmoonsunlat = float(moonlat) - float(sunlat)


    if diffmoonsunlat < 0:
        thitinumber = math.ceil((diffmoonsunlat + 360) / 12)
        diffmoonsunlat = diffmoonsunlat + 360
    else:
        thitinumber = math.ceil((diffmoonsunlat) / 12)


    firstorsecond=""

    if diffmoonsunlat > 0 and diffmoonsunlat <= 6:
        firstorsecond = 1
    elif diffmoonsunlat > 6 and diffmoonsunlat <= 12:
        firstorsecond = 2
    elif diffmoonsunlat > 12 and diffmoonsunlat <= 18:
        firstorsecond = 1
    elif diffmoonsunlat > 18 and diffmoonsunlat <= 24:
        firstorsecond = 2
    elif diffmoonsunlat > 24 and diffmoonsunlat <= 30:
        firstorsecond = 1
    elif diffmoonsunlat > 30 and diffmoonsunlat <= 36:
        firstorsecond = 2
    elif diffmoonsunlat > 36 and diffmoonsunlat <= 42:
        firstorsecond = 1
    elif diffmoonsunlat > 42 and diffmoonsunlat <= 48:
        firstorsecond = 2
    elif diffmoonsunlat > 48 and diffmoonsunlat <= 54:
        firstorsecond = 1
    elif diffmoonsunlat > 54 and diffmoonsunlat <= 60:
        firstorsecond = 2
    elif diffmoonsunlat > 60 and diffmoonsunlat <= 66:
        firstorsecond = 1
    elif diffmoonsunlat > 66 and diffmoonsunlat <= 72:
        firstorsecond = 2
    elif diffmoonsunlat > 72 and diffmoonsunlat <= 78:
        firstorsecond = 1
    elif diffmoonsunlat > 78 and diffmoonsunlat <= 84:
        firstorsecond = 2
    elif diffmoonsunlat > 84 and diffmoonsunlat <= 90:
        firstorsecond = 1
    elif diffmoonsunlat > 90 and diffmoonsunlat <= 96:
        firstorsecond = 2
    elif diffmoonsunlat > 96 and diffmoonsunlat <= 102:
        firstorsecond = 1
    elif diffmoonsunlat > 102 and diffmoonsunlat <= 108:
        firstorsecond = 2
    elif diffmoonsunlat > 108 and diffmoonsunlat <= 114:
        firstorsecond = 1
    elif diffmoonsunlat > 114 and diffmoonsunlat <= 120:
        firstorsecond = 2
    elif diffmoonsunlat > 120 and diffmoonsunlat <= 126:
        firstorsecond = 1
    elif diffmoonsunlat > 126 and diffmoonsunlat <= 132:
        firstorsecond = 2
    elif diffmoonsunlat > 132 and diffmoonsunlat <= 138:
        firstorsecond = 1
    elif diffmoonsunlat > 138 and diffmoonsunlat <= 144:
        firstorsecond = 2
    elif diffmoonsunlat > 144 and diffmoonsunlat <= 150:
        firstorsecond = 1
    elif diffmoonsunlat > 150 and diffmoonsunlat <= 156:
        firstorsecond = 2
    elif diffmoonsunlat > 156 and diffmoonsunlat <= 162:
        firstorsecond = 1
    elif diffmoonsunlat > 162 and diffmoonsunlat <= 168:
        firstorsecond = 2
    elif diffmoonsunlat > 168 and diffmoonsunlat <= 174:
        firstorsecond = 1
    elif diffmoonsunlat > 174 and diffmoonsunlat <= 180:
        firstorsecond = 2
    elif diffmoonsunlat > 180 and diffmoonsunlat <= 186:
        firstorsecond = 1
    elif diffmoonsunlat > 186 and diffmoonsunlat <= 192:
        firstorsecond = 2
    elif diffmoonsunlat > 192 and diffmoonsunlat <= 198:
        firstorsecond = 1
    elif diffmoonsunlat > 198 and diffmoonsunlat <= 204:
        firstorsecond = 2
    elif diffmoonsunlat > 204 and diffmoonsunlat <= 210:
        firstorsecond = 1
    elif diffmoonsunlat > 210 and diffmoonsunlat <= 216:
        firstorsecond = 2
    elif diffmoonsunlat > 216 and diffmoonsunlat <= 222:
        firstorsecond = 1
    elif diffmoonsunlat > 222 and diffmoonsunlat <= 228:
        firstorsecond = 2
    elif diffmoonsunlat > 228 and diffmoonsunlat <= 234:
        firstorsecond = 1
    elif diffmoonsunlat > 234 and diffmoonsunlat <= 240:
        firstorsecond = 2
    elif diffmoonsunlat > 240 and diffmoonsunlat <= 246:
        firstorsecond = 1
    elif diffmoonsunlat > 246 and diffmoonsunlat <= 252:
        firstorsecond = 2
    elif diffmoonsunlat > 252 and diffmoonsunlat <= 258:
        firstorsecond = 1
    elif diffmoonsunlat > 258 and diffmoonsunlat <= 264:
        firstorsecond = 2
    elif diffmoonsunlat > 264 and diffmoonsunlat <= 270:
        firstorsecond = 1
    elif diffmoonsunlat > 270 and diffmoonsunlat <= 276:
        firstorsecond = 2
    elif diffmoonsunlat > 276 and diffmoonsunlat <= 282:
        firstorsecond = 1
    elif diffmoonsunlat > 282 and diffmoonsunlat <= 288:
        firstorsecond = 2
    elif diffmoonsunlat > 288 and diffmoonsunlat <= 294:
        firstorsecond = 1
    elif diffmoonsunlat > 294 and diffmoonsunlat <= 300:
        firstorsecond = 2
    elif diffmoonsunlat > 300 and diffmoonsunlat <= 306:
        firstorsecond = 1
    elif diffmoonsunlat > 306 and diffmoonsunlat <= 312:
        firstorsecond = 2
    elif diffmoonsunlat > 312 and diffmoonsunlat <= 318:
        firstorsecond = 1
    elif diffmoonsunlat > 318 and diffmoonsunlat <= 324:
        firstorsecond = 2
    elif diffmoonsunlat > 324 and diffmoonsunlat <= 330:
        firstorsecond = 1
    elif diffmoonsunlat > 330 and diffmoonsunlat <= 336:
        firstorsecond = 2
    elif diffmoonsunlat > 336 and diffmoonsunlat <= 342:
        firstorsecond = 1
    elif diffmoonsunlat > 342 and diffmoonsunlat <= 348:
        firstorsecond = 2
    elif diffmoonsunlat > 348 and diffmoonsunlat <= 354:
        firstorsecond = 1
    elif diffmoonsunlat > 354 and diffmoonsunlat <= 360:
        firstorsecond = 2

    #print("Thithi Number: " + str(thitinumber))

    if language=="english":
        if firstorsecond == 1:
            return thithi_first[thitinumber]
        elif firstorsecond == 2:
            return thithi_second[thitinumber]
    elif language=="tamil":
        if firstorsecond == 1:
            return thithi_first_tamil[thitinumber]
        elif firstorsecond == 2:
            return thithi_second_tamil[thitinumber]
            

def tamilday(weekday):
    if weekday=="Monday":
        tamilstr="திங்கள் "
    elif weekday=="Tuesday":
        tamilstr="செவ்வாய்"
    elif weekday=="Wednesday":
        tamilstr="புதன்"
    elif weekday=="Thursday":
        tamilstr="வியாழன்"
    elif weekday=="Friday":
        tamilstr="வெள்ளி "
    elif weekday=="Saturday":
        tamilstr="சனி"        
    elif weekday=="Sunday":
        tamilstr="ஞாயிறு "

    return tamilstr
        

def star_start_degree(star):
    if star == "ASWINI":
        deg = 0
    elif star == "BHARANI":
        deg = 13.33333333
    elif star == "KIRUTHIGAI":
        deg = 26.66666667
    elif star == "ROGINI":
        deg = 40
    elif star == "MIRUGASEERASAM":
        deg = 53.33333333
    elif star == "THIRUVAADHIRAI":
        deg = 66.66666667
    elif star == "PUNARPOOSAM":
        deg = 80
    elif star == "POOSAM":
        deg = 93.33333333
    elif star == "AYILYAM":
        deg = 106.6666667
    elif star == "MAGAM":
        deg = 120
    elif star == "POORAM":
        deg = 133.3333333
    elif star == "UTHRAM":
        deg = 146.6666667
    elif star == "HASTHAM":
        deg = 160
    elif star == "SITHIRAI":
        deg = 173.3333333
    elif star == "SUVATHI":
        deg = 186.6666667
    elif star == "VISAAGAM":
        deg = 200
    elif star == "ANUSAM":
        deg = 213.3333333
    elif star == "KETTAI":
        deg = 226.6666667
    elif star == "MOOLAM":
        deg = 240
    elif star == "POORAADAM":
        deg = 253.3333333
    elif star == "UTHIRAADAM":
        deg = 266.6666667
    elif star == "THIRUVONAM":
        deg = 280
    elif star == "AVITTAM":
        deg = 23.3333333
    elif star == "SADAYAM":
        deg = 306.6666667
    elif star == "POORATTAADHI":
        deg = 320
    elif star == "UTHRATTAADHI":
        deg = 333.3333333
    elif star == "REVATHI":
        deg = 346.6666667
        
    
    return deg
    
    
def starlorddasa(star):    
    if star == "ASWINI":
        deg = 7
    elif star == "BHARANI":
        deg = 20
    elif star == "KIRUTHIGAI":
        deg = 6
    elif star == "ROGINI":
        deg = 10
    elif star == "MIRUGASEERASAM":
        deg = 7
    elif star == "THIRUVAADHIRAI":
        deg = 18
    elif star == "PUNARPOOSAM":
        deg = 16
    elif star == "POOSAM":
        deg = 19
    elif star == "AYILYAM":
        deg = 17
    elif star == "MAGAM":
        deg = 7
    elif star == "POORAM":
        deg = 20
    elif star == "UTHRAM":
        deg = 6
    elif star == "HASTHAM":
        deg = 10
    elif star == "SITHIRAI":
        deg = 7
    elif star == "SUVATHI":
        deg = 18
    elif star == "VISAAGAM":
        deg = 16
    elif star == "ANUSAM":
        deg = 19
    elif star == "KETTAI":
        deg = 17
    elif star == "MOOLAM":
        deg = 7
    elif star == "POORAADAM":
        deg = 20
    elif star == "UTHIRAADAM":
        deg = 6
    elif star == "THIRUVONAM":
        deg = 10
    elif star == "AVITTAM":
        deg = 7
    elif star == "SADAYAM":
        deg = 18
    elif star == "POORATTAADHI":
        deg = 16
    elif star == "UTHRATTAADHI":
        deg = 19
    elif star == "REVATHI":
        deg = 17
        
    
    return deg    
    

def Get_Bhukthi_Year_Month_Days(startdate, idasayear, ibhukthiyear):
    temp = idasayear * ibhukthiyear / 120
    year =  round(temp)
    month = (temp - year) * 12
    temp1 = month - round(month)
    days = temp1 * 30
    #print ("")
    #print (str(year) + " years " + str(round(month)) + " months " + str(round(days)) + " days")
    
    add_days = startdate + relativedelta(days=+round(days))
    add_months = add_days + relativedelta(months=+round(month))
    add_years = add_months + relativedelta(years=+year)    
    return (add_years)

    
def Get_Anthram_Year_Month_Days(startdate, idasayear, ibhukthiyear, ianthramyear):
    temp = (idasayear * ibhukthiyear * ianthramyear) / (120 * 120)
    year = round(temp)
    month = (temp - year) * 12
    temp1 = month - round(month)
    days = temp1 * 30

    add_days = startdate + relativedelta(days=+round(days))
    add_months = add_days + relativedelta(months=+round(month))
    add_years = add_months + relativedelta(years=+year) 
    return (add_years)    


  
def dasabhukthi(moonlat, birthdate):

    star = star_query(moonlat)
    starloard = star_lord(moonlat)
    diffrence = (moonlat - star_start_degree(star)) / 13.333333333333334
    starloarddasa = starlorddasa(star)
    consumeddasayear = diffrence * starloarddasa;
    tdec = math.floor(consumeddasayear)
    tdec1 = consumeddasayear - tdec
    consumedmonths = tdec1 * 12
    tdec2 = math.floor(consumedmonths)
    tdec3 = consumedmonths - tdec2
    consumeddays = (tdec3 * 365.25) / 12
    tdec4 = math.floor(consumeddays)
    #consumedperiod = "-" . tdec . " years -" . tdec2 . " months -" . tdec4 . " days"
    tdec5 = (tdec * 365.25) + (tdec2 * 30) + tdec4
    tdec6 = starloarddasa * 365.25
    tdec7 = tdec6 - tdec5
    totalconsumeddays = (tdec * 365.25) + (tdec2 * 30) + tdec4
    tdec8 = tdec7 / 365.25
    tdec9 = math.floor(tdec8)
    tdec10 = (tdec8 - tdec9) * 12
    tdec11 = math.floor(tdec10)
    tdec12 = tdec10 - tdec11
    tdec13 = (tdec12 * 365.25) / 12
    tdec14 = math.floor(tdec13)

    
    kethu_planets_vimsottari_order = ["0","Ke","Ve","Su","Mo","Ma","Ra","Ju","Sa","Me"]
    kethu_planets_vimsottari_dasayears = ["0","7","20","6","10","7","18","16","19","17"]

    venus_planets_vimsottari_order = ["0","Ve","Su","Mo","Ma","Ra","Ju","Sa","Me","Ke"]
    venus_planets_vimsottari_dasayears = ["0","20","6","10","7","18","16","19","17","7"]

    sun_planets_vimsottari_order = ["0","Su","Mo","Ma","Ra","Ju","Sa","Me","Ke","Ve"]
    sun_planets_vimsottari_dasayears = ["0","6","10","7","18","16","19","17","7","20"]

    moon_planets_vimsottari_order = ["0","Mo","Ma","Ra","Ju","Sa","Me","Ke","Ve","Su"]
    moon_planets_vimsottari_dasayears = ["0","10","7","18","16","19","17","7","20","6"]

    mars_planets_vimsottari_order = ["0","Ma","Ra","Ju","Sa","Me","Ke","Ve","Su","Mo"]
    mars_planets_vimsottari_dasayears = ["0","7","18","16","19","17","7","20","6","10"]

    raghu_planets_vimsottari_order = ["0","Ra","Ju","Sa","Me","Ke","Ve","Su","Mo","Ma"]
    raghu_planets_vimsottari_dasayears = ["0","18","16","19","17","7","20","6","10","7"]

    guru_planets_vimsottari_order = ["0","Ju","Sa","Me","Ke","Ve","Su","Mo","Ma","Ra"]
    guru_planets_vimsottari_dasayears = ["0","16","19","17","7","20","6","10","7","18"]

    sani_planets_vimsottari_order = ["0","Sa","Me","Ke","Ve","Su","Mo","Ma","Ra","Ju"]
    sani_planets_vimsottari_dasayears = ["0","19","17","7","20","6","10","7","18","16"]

    bhudhan_planets_vimsottari_order = ["0","Me","Ke","Ve","Su","Mo","Ma","Ra","Ju","Sa"]
    bhudhan_planets_vimsottari_dasayears = ["0","17","7","20","6","10","7","18","16","19"]

    if starloard == "Kethu":
        pname = kethu_planets_vimsottari_order
        v_dasa = kethu_planets_vimsottari_dasayears
    elif starloard == "Venus":
        pname = venus_planets_vimsottari_order
        v_dasa = venus_planets_vimsottari_dasayears
    elif starloard == "Sun":
        pname = sun_planets_vimsottari_order
        v_dasa = sun_planets_vimsottari_dasayears    
    elif starloard == "Moon":
        pname = moon_planets_vimsottari_order
        v_dasa = moon_planets_vimsottari_dasayears    
    elif starloard == "Mars":
        pname = mars_planets_vimsottari_order
        v_dasa = mars_planets_vimsottari_dasayears    
    elif starloard == "Raghu":
        pname = raghu_planets_vimsottari_order
        v_dasa = raghu_planets_vimsottari_dasayears    
    elif starloard == "Jupiter":
        pname = guru_planets_vimsottari_order
        v_dasa = guru_planets_vimsottari_dasayears        
    elif starloard == "Saturn":
        pname = sani_planets_vimsottari_order
        v_dasa = sani_planets_vimsottari_dasayears        
    elif starloard == "Mercury":
        pname = bhudhan_planets_vimsottari_order
        v_dasa = bhudhan_planets_vimsottari_dasayears                                        


    idasaLord = 0
    ibhuktiLord = 0
    iantraLord = 0
    SN = 0
    result = ""
    p1 = 0
    p2 = 0
    bhuktilength = 0

    birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y')
    #print (birthdate)
    
    sub_days = birthdate + relativedelta(days=-tdec4)
    sub_months = sub_days + relativedelta(months=-tdec2)
    sub_years = sub_months + relativedelta(years=-tdec)
    
    startdate = sub_years
    #print ("Start Date : " + str(startdate))
    
    result="<table><tr><td>Dasa</td><td>Anthra Dasa</td><td>Start</td><td>End</td><td>Priyanthra Dasa</td><td>Start</td><td>End</td></tr>"
    
    for idasa in range(1, 10):
        #result = result + "\n***** idasa = " + str(idasa) + " ***** " + pname[idasa] + "\n"
        
        for ibhukti in range(9):
            ibhuktiLord = idasa + ibhukti
            if ibhuktiLord > 9:
                ibhuktiLord = ibhuktiLord - 9
 
            enddate = Get_Bhukthi_Year_Month_Days(startdate, int(v_dasa[idasa]),int(v_dasa[ibhuktiLord]))
            
            #result = result + "<tr><td>" + pname[idasa] + "</td><td>" + pname[ibhuktiLord] + "</td><td>" + str(startdate.strftime('%d-%m-%Y')) + "</td><td>" + str(enddate.strftime('%d-%m-%Y')) + "</td></tr>"

            antharamstartdate = startdate

            for ianthra in range(9):
                ianthraLord = ibhuktiLord + ianthra
                if ianthraLord > 9:
                    ianthraLord = ianthraLord - 9
            
                anthramperiod = Get_Anthram_Year_Month_Days(startdate,int(v_dasa[idasa]),int(v_dasa[ibhuktiLord]), int(v_dasa[ianthraLord]))    

                if ianthra == 8:
                    antharamenddate = enddate
                else:
                    antharamenddate = anthramperiod
                    
                result = result + "<tr><td>" + pname[idasa] + "</td><td>" + pname[ibhuktiLord] + "</td><td>" + str(startdate.strftime('%d-%m-%Y')) + "</td><td>" + str(enddate.strftime('%d-%m-%Y')) + "</td><td>" + pname[ianthraLord] + "</td><td>" + str(antharamstartdate.strftime('%d-%m-%Y')) + "</td><td>" + str(antharamenddate.strftime('%d-%m-%Y')) + "</td></tr>"
            
            #result = result + "\n"
            startdate = enddate
            

    result = result + "</table>"
    return (result)
    

def nameletterstamil(star):    
    
    starletters=""
    
    if star == "ASWINI":
        starletters = "சு, கே, சோ, ல"
    elif star == "BHARANI":
        starletters = "லி, லு, லே, லோ"
    elif star == "KIRUTHIGAI":
        starletters = "அ, இ, உ, எ"
    elif star == "ROGINI":
        starletters = "ஒ, வ, வி, வூ"
    elif star == "MIRUGASEERASAM":
        starletters = "வே, வோ, க், கி"
    elif star == "THIRUVAADHIRAI":
        starletters = "கு, த, ங், ச"
    elif star == "PUNARPOOSAM":
        starletters = "கே, கோ, ஹ, ஹி"
    elif star == "POOSAM":
        starletters = "ஹூ, ஹே, ஹோ, ட"
    elif star == "AYILYAM":
        starletters = "டி, டு, டே, டோ"
    elif star == "MAGAM":
        starletters = "ம, மி, மு, மே"
    elif star == "POORAM":
        starletters = "மோ, ட, டி, டு"
    elif star == "UTHRAM":
        starletters = "டே, டோ, ப, பி"
    elif star == "HASTHAM":
        starletters = "பு, ஷ, ண, ட"
    elif star == "SITHIRAI":
        starletters = "பே, போ, ர, ரி"
    elif star == "SUVATHI":
        starletters = "ரு, ரே, ரோ, தா"
    elif star == "VISAAGAM":
        starletters = "தி, து, தே, தோ"
    elif star == "ANUSAM":
        starletters = "க, நி, து, நே"
    elif star == "KETTAI":
        starletters = "நோ, யா, யீ, யு"
    elif star == "MOOLAM":
        starletters = "யே, யோ, ப, பி"
    elif star == "POORAADAM":
        starletters = "பு, த, ப, ட"
    elif star == "UTHIRAADAM":
        starletters = "பே, போ, ஜ, ஜி"
    elif star == "THIRUVONAM":
        starletters = "கி, கு, கே, கோ"
    elif star == "AVITTAM":
        starletters = "க, கி, கு, கே"
    elif star == "SADAYAM":
        starletters = "கோ, ஸ, ஸி, ஸே"
    elif star == "POORATTAADHI":
        starletters = "ஸோ, ஸோ, த, தி"
    elif star == "UTHRATTAADHI":
        starletters = "து, ஸ்ரீ, ச, த"
    elif star == "REVATHI":
        starletters = "தே, தோ, ச, சி"
        
    return starletters   
    
    
def namelettersenglish(star):    
    
    starletters=""
    
    if star == "ASWINI":
        starletters = "Chu, Che, Cho, Choo, La, Laa"
    elif star == "BHARANI":
        starletters = "Li, Lu, Le, Lo, Lee"
    elif star == "KIRUTHIGAI":
        starletters = "Aa, Ae, E, Ee, Ai, A, I, Oo, U"
    elif star == "ROGINI":
        starletters = "O, Va, Vaa, Vi, Vee, Vu, Voo, Wa, Wu"
    elif star == "MIRUGASEERASAM":
        starletters = "Ve, Vo, Ka, Kaa, Ki Kee, We, Wo"
    elif star == "THIRUVAADHIRAI":
        starletters = "Ku, Kam, Ja, Cha, Gha, Da, Na, Jha"
    elif star == "PUNARPOOSAM":
        starletters = "Ke, Kay Ko, Ha, Hi, Hee"
    elif star == "POOSAM":
        starletters = "Hu, He, Ho, Da"
    elif star == "AYILYAM":
        starletters = "Di, Du, De, Do, Dee, Me, Da"
    elif star == "MAGAM":
        starletters = "Ma,Maa, Mi, Mee Mu, Me"
    elif star == "POORAM":
        starletters = "Mo, Ta, Taa, Ti, Tee, Tu"
    elif star == "UTHRAM":
        starletters = "Te, Ta, Taa, To, Pa, Paa, Pi, Pee"
    elif star == "HASTHAM":
        starletters = "Pu, Sha, Shaa, Na, Poo, Tha"
    elif star == "SITHIRAI":
        starletters = "Pe, Po, Ra, Raa, Ri, Ree"
    elif star == "SUVATHI":
        starletters = "Ru, Re, Ro, Roo, Ta, Taa"
    elif star == "VISAAGAM":
        starletters = "Ti, Tee, Too, Te, Tu, Tae, To"
    elif star == "ANUSAM":
        starletters = "Na, Naa, Ni, Nu, Ne, Nee, Noo, Nae"
    elif star == "KETTAI":
        starletters = "No, Ya, Yaa, Yi, Yu, Yee"
    elif star == "MOOLAM":
        starletters = "Ye, Yu, Ba, Bi, Yo, Bhi, Bha, Bhaa, Bhee"
    elif star == "POORAADAM":
        starletters = "Bu, Da, Bhoo, Pha, Dha, Fa"
    elif star == "UTHIRAADAM":
        starletters = "Be, Bo, Ja, Ji, Bha, Bhe, Bho, Jaa, Jee"
    elif star == "THIRUVONAM":
        starletters = "Ju, Je, Jo, Khi , So, Khu, Khe, Kho"
    elif star == "AVITTAM":
        starletters = "    Ga, Gi, Gu, Ge, Gee"
    elif star == "SADAYAM":
        starletters = "Go, Sa, Saa, Si, Su, Soo, See, Gau"
    elif star == "POORATTAADHI":
        starletters = "Se, So, Dha, Dhi, Di, Da, Daa, Dee"
    elif star == "UTHRATTAADHI":
        starletters = "Du, Tha, Jha, Na, Gna, Jna, Da, Gy"
    elif star == "REVATHI":
        starletters = "De, Do, Cha, Chaa, Chi, Chee"
        
    return starletters   
    

def startreestamil(star):    
    
    starletters=""
    
    if star == "ASWINI":
        starletters = "காஞ்சிதை, மகிழம்,<br>பாதாம், நண்டாஞ்சு"
    elif star == "BHARANI":
        starletters = "அத்தி, மஞ்சக்கடம்பு, <br>விளா, நந்தியாவட்டை"
    elif star == "KIRUTHIGAI":
        starletters = "நெல்லி, மணிபுங்கம், <br>வெண் தேக்கு, நிரிவேங்கை"
    elif star == "ROGINI":
        starletters = "நாவல், சிவப்பு மந்தாரை, <br>மந்தாரை, நாகலிங்கம்"
    elif star == "MIRUGASEERASAM":
        starletters = "கருங்காலி, ஆச்சா, <br>வேம்பு, நீர்க்கடம்பு"
    elif star == "THIRUVAADHIRAI":
        starletters = "செங்கருங்காலி, வெள்ளை, <br>வெள்ளெருக்கு, வெள்ளெருக்கு"
    elif star == "PUNARPOOSAM":
        starletters = "மூங்கில், மலைவேம்பு, <br>அடப்பமரம், நெல்லி"
    elif star == "POOSAM":
        starletters = "அரசு, ஆச்சா, <br>இருள், நொச்சி"
    elif star == "AYILYAM":
        starletters = "புன்னை, முசுக்கட்டை, <br>இலந்தை, பலா"
    elif star == "MAGAM":
        starletters = "ஆலமரம், முத்திலா மரம், <br>இலுப்பை, பவளமல்லி"
    elif star == "POORAM":
        starletters = "பலா, வாகை, <br>ருத்திராட்சம், பலா"
    elif star == "UTHRAM":
        starletters = "ஆலசி, வாதநாராயணன், <br>எட்டி, புங்கமரம்"
    elif star == "HASTHAM":
        starletters = "ஆத்தி, தென்னை, <br>ஓதியன், புத்திரசீவி"
    elif star == "SITHIRAI":
        starletters = "வில்வம், புரசு, <br>கொடுக்காபுளி, தங்க அரளி"
    elif star == "SUVATHI":
        starletters = "மருது, புளி, மஞ்சள் கொன்றை, <br>கொழுக்கட்டை மந்தாரை"
    elif star == "VISAAGAM":
        starletters = "விளா, சிம்சுபா, <br>பூவன், தூங்குமூஞ்சி"
    elif star == "ANUSAM":
        starletters = "மகிழம், பூமருது, <br>கொங்கு, தேக்கு"
    elif star == "KETTAI":
        starletters = "பலா, பூவரசு, <br>அரசு, வேம்பு"
    elif star == "MOOLAM":
        starletters = "மராமரம், பெரு, <br>செண்பக மரம், ஆச்சா"
    elif star == "POORAADAM":
        starletters = "வஞ்சி, கடற்கொஞ்சி, <br>சந்தானம், எலுமிச்சை"
    elif star == "UTHIRAADAM":
        starletters = "பலா, கடுக்காய், <br>சாரப்பருப்பு, தாளை"
    elif star == "THIRUVONAM":
        starletters = "வெள்ளெருக்கு, கருங்காலி, <br>சிறுநாகப்பூ, பாக்கு"
    elif star == "AVITTAM":
        starletters = "வன்னி, கருவேல், <br>சீத்தா, ஜாதிக்காய்"
    elif star == "SADAYAM":
        starletters = "கடம்பு, பரம்பை, <br>ராம்சீதா, திலகமரம்"
    elif star == "POORATTAADHI":
        starletters = "தேமா, குங்கிலியம், <br>சுந்தரவேம்பு, கன்னிமந்தாரை"
    elif star == "UTHRATTAADHI":
        starletters = "வேம்பு, குல்மோகர், <br>சேராங்கொட்டை, செம்மரம்"
    elif star == "REVATHI":
        starletters = "பனை, தங்க அரளி, <br>செஞ்சந்தனம், மஞ்சபலா"
        
    return starletters   
	

def startreesenglish(star):    
    
    starletters=""
    
    if star == "ASWINI":
        starletters = "Strychnine Tree, <br>Indian Medlar, Almond, Nandaanju"
    elif star == "BHARANI":
        starletters = "Fig Tree, Haldu, <br>Wood Apple, Crape jasmine"
    elif star == "KIRUTHIGAI":
        starletters = "Gooseberry, Notched Leaf Soapnut, <br>Ben Teak, Sandan"
    elif star == "ROGINI":
        starletters = "Java Plum, Orchid Tree, <br>Maloo Creeper, Cannan Ball Tree"
    elif star == "MIRUGASEERASAM":
        starletters = "Indian Ebony, Anjan, <br>Neem, Kaim"
    elif star == "THIRUVAADHIRAI":
        starletters = "Cutch Tree, Cork Bush, <br>Rubber Bush, sodom apple"
    elif star == "PUNARPOOSAM":
        starletters = "Indian Thorny Bamboo, <br>Malabar Neem, Badam, Gooseberry"
    elif star == "POOSAM":
        starletters = "Peepal, Anjan, <br>Burma Ironwood, Chaste Tree"
    elif star == "AYILYAM":
        starletters = "Beauty Leaf, White Mulberry, <br>Jujube tree, Jackfruit"
    elif star == "MAGAM":
        starletters = "Banyan tree, Muthila, <br>Indian Butter Tree, Har singar"
    elif star == "POORAM":
        starletters = "Jackfruit, Siris tree, <br>Ceylon Olive, Jackfruit"
    elif star == "UTHRAM":
        starletters = "Flax, White Gulmohar, <br>Strychnine Tree, Pongam Tree"
    elif star == "HASTHAM":
        starletters = "Bidi Leaf Tree, Coconut, <br>Othiyan, Putranjiva"
    elif star == "SITHIRAI":
        starletters = "Bel, Flame of the forest, <br>Manilla Tamarind, Mexican oleander"
    elif star == "SUVATHI":
        starletters = "Pride of India, Tamarind, <br>Siamese Senna, St.Thomas tree"
    elif star == "VISAAGAM":
        starletters = "Wood Apple, Indian rosewood, <br>Mysore banana, Rain Tree"
    elif star == "ANUSAM":
        starletters = "Indian Medlar, Queen Crape Myrtle, <br>Ponga, Teak"
    elif star == "KETTAI":
        starletters = "Jackfruit, Aden apple, <br>Peepal, Neem"
    elif star == "MOOLAM":
        starletters = "Sal, Indian Tree of Heaven, <br>Champa, Anjan"
    elif star == "POORAADAM":
        starletters = "Indian Willow, chinese box, <br>Sandalwood, Lemon"
    elif star == "UTHIRAADAM":
        starletters = "Jackfruit, Chebulic Myrobalan, <br>Cuddapah Almond, Kewda"
    elif star == "THIRUVONAM":
        starletters = "French cotton, Indian Ebony, <br>Cobra saffron, Betel Palm"
    elif star == "AVITTAM":
        starletters = "Rusty Acacia, Gum Arabic, <br>Custard apple, Nutmeg"
    elif star == "SADAYAM":
        starletters = "Barringtonia, Khejri Tree, <br>Netted Custard Apple, Red Sandalwood"
    elif star == "POORATTAADHI":
        starletters = "Mango, Sal, <br>Neem, Maloo Creeper"
    elif star == "UTHRATTAADHI":
        starletters = "Neem, Flamboyant, <br>Marking Nut, Pithraj Tree"
    elif star == "REVATHI":
        starletters = "Palmyra Palm, Mexican oleander, <br>Red sandalwood, Jackfruit"
        
    return starletters   