#!/user/etc/env python3
import math
# 海平面的值	参照值	_SL	
T_SL=2.8815*(10**2)     # °K
P_SL=1.01325*(10**5)    # Pa
density_SL=1.225        # kg/m^3
g_SL=9.80665            # m/s^2
Mach_SL=3.40294*(10**2) # 

def density(h=0):
    H=h/1000                # H单位由h的m变为km
    R0=6.356766*(10**3)     # km
    Z=H/(1-H/R0)            # km
    
    if (Z>=0)and(Z<=11.0191):
        W=1-H/44.3308
        Den=density_SL*(W**4.2559)
    elif (Z>11.0191)and(Z<=20.0631):
        W=math.exp((14.9647-H)/6.3416)
        Den=density_SL*1.5898*(10**-1)*W    
    elif (Z>20.0631)and(Z<=32.1619):
        W=1+(H-24.9021)/221.552
        Den=density_SL*3.2722*(10**-2)*(W**-35.1629)        
    elif (Z>32.1619)and(Z<=47.3501):
        W=1+(H-39.7499)/89.4107;
        Den=density_SL*3.2618*(10**-3)*(W**-13.2011)        
    elif (Z>47.3501)and(Z<=51.4125):
        W=math.exp((48.6252-H)/7.9223)
        Den=density_SL*9.4920*(10**-4)*W        
    elif (Z>51.4125)and(Z<=71.8020):
        W=1-(H-59.4390)/88.2218
        Den=density_SL*2.5280*(10**-4)*(W**11.2011)        
    elif (Z>71.8020)and(Z<86):
        W=1-(H-78.0303)/100.2950
        Den=density_SL*1.7632*(10**-5)*(W**16.0816)        
    elif (Z>=86)and(Z<=91):
        W=math.exp((87.2848-H)/5.2700)
        Den=density_SL*3.6411*(10**-6)*W   
    else :
        print('Error')
    return Den
	
# '''
#     if (Z>=0)and(Z<=11.0191):
#         {
#             W=1-H/44.3308;
# 			T = 288.15*W;
# 			P = P_SL*pow(W,5.2559);
#             density = density_SL*pow(W,4.2559);
#         }
#     else if ((Z>11.0191)||(Z<=20.0631))
#         {
#             W=math.exp((14.9647-H)/6.3416);
# 			T = 216.650;
# 			P = P_SL*1.1953*pow(10,-1)*W;
#             density=density_SL*1.5898*pow(10,-1)*W;
#         }
#     else if ((Z>20.0631)||(Z<=32.1619))
#         {
#             W=1+(H-24.9021)/221.552;
#             T = 221.552*W;
# 			P = P_SL*2.5158*pow(10,-2)*pow(W,-34.1629);
# 			density=density_SL*3.2722*pow(10,-2)*pow(W,-35.1629);
#         }
#     else if ((Z>32.1619)||(Z<=47.3501))
#         {
#             W=1+(H-39.7499)/89.4107;
# 			T = 250.350 * W;
# 			P = P_SL*2.8338*pow(10,-3)*pow(W,-12.2011);
#             density=density_SL*3.2618*pow(10,-3)*pow(W,-13.2011);
#         }
#     else if ((Z>47.3501)||(Z<=51.4125))
#         {
#             W=math.exp((48.6252-H)/7.9223);
# 			T = 270.650;
# 			P = P_SL*8.9115*pow(10,-4)*W;
#             density=density_SL*9.4920*pow(10,-4)*W;
#         }
#     else if ((Z>51.4125)||(Z<=71.8020))
#         {
#             W=1-(H-59.4390)/88.2218;
# 			T = 247.021 * W;
# 			P = P_SL*2.1671*pow(10,-4)*pow(W,12.2011);
#             density=density_SL*2.5280*pow(10,-4)*pow(W,11.2011);
#         }
#     else if ((Z>71.8020)||(Z<86))
#         {
#             W=1-(H-78.0303)/100.2950;
# 			T = 200.590 * W;
# 			P = P_SL*1.2274*pow(10,-5)*pow(W,17.0816);
#             density=density_SL*1.7632*pow(10,-5)*pow(W,16.0816);
#         }
#     else if ((Z>=86)||(Z<=91))
#         {
#             W=math.exp((87.2848-H)/5.2700);
# 			T = 186.870;
# 			P = P_SL*(2.2730+1.042*pow(10,-3)*H)*pow(10,-6)*W;
#             density=density_SL*3.6411*pow(10,-6)*W;
#         }

# 	g=g_SL/pow( (1 + Z / ( 6.356766*pow(10,3) ) ),2);
# 	Mach= 20.0468*sqrt(T);
	
# 	atmsph[0]=T; //°K
# 	// atmsph[0]=T;//℃
# 	atmsph[1]=P;
# 	atmsph[2]=density;
# 	atmsph[3]=g;
# 	atmsph[4]=Mach;
	
# 	return atmsph;
# }
# '''