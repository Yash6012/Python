import statistics
import math

def fn(a,b):
    print("\nYou've chosen to find out about the {} & the {} stock".format(x.upper(),y.upper()))
    avgA=[]
    i=0
    j=0
    while i<5 and j<5:
        avgsa=((a[0][i])+(a[1][j]))/2
        avgA.append(avgsa)
        i+=1
        j+=1

    avgB=[]
    k=0
    l=0
    while k<5 and l<5:
        avgsb=((b[0][k])+(b[1][l]))/2
        avgB.append(avgsb)
        k+=1
        l+=1

    Am=statistics.mean(avgA)
    Bm=statistics.mean(avgB)

    mxv=[]
    o=0
    while o<5:
        ixm=((avgA[o])-Am)
        mxv.append(ixm)
        o+=1

    myv=[]
    p=0
    while p<5:
        ixm=((avgA[p])-Bm)
        myv.append(ixm)
        p+=1

    dxy=[]
    q=0
    r=0
    while q<5 and r<5:
        xy=((mxv[q])*(myv[r]))
        dxy.append(xy)
        q+=1
        r+=1

    dxysq=[]
    s=0
    while s<5:
        sq=(dxy[s])**2
        dxysq.append(sq)
        s+=1

    dxysqa=sum(dxysq)
    dxysqar=math.sqrt(dxysqa)

    tfl=[]
    t=0
    while t<5:
        tlv=(dxy[t])/dxysqar
        tfl.append(tlv)
        t+=1

    corr=sum(tfl)/len(tfl)
    print('\33[1mThe correlation between {} & {} is {}'.format(x.upper(),y.upper(),corr))

print('Hello, Here we have 6 Blue-chip Stocks and their NSE 5 day price histories,\nyou can consider these for intraday trades')
print('The prices are real time prices between 04/05/2023 to 10/05/2023')
print('Choose between Reliance, Asian Paints, HDFC, TCS, ITC & Infosys')
print('\n')

ril=[[2446,2459,2478.10,2483.35,2496.7],[2429,2439,2456,2467.15,2488.2]]
ap=[[2982,3019,3029.75,3071,3050.3],[2931,2960,2997,3025,3028]]
hdfc=[[1729,1650,1649.7,1653.75,1652.3],[1693,1627,1645,1642.75,1637.5]]
tcs=[[3219.45,3236,3251.5,3292,3291.35],[3196.45,3213.25,3236,3250.65,3278]]
itc=[[425.55,430,432.30,432.10,426],[424.15,425.45,430.35,423.15,423.2]]
infy=[[1274,1269,1270,1271.55,1266],[1267,1255.25,1257.6,1262.9,1260]]

x,y=input('Enter names of two shares from above to calculate co-relation: ').split()

if x in 'relianceRELIANCEReliance' and y in 'asian paintsASIAN PAINTSAsian Paints':
    fn(ril,ap)
if x in 'relianceRELIANCEReliance' and y in 'hdfcHDFCHdfc':
    fn(ril,hdfc)
if x in 'relianceRELIANCEReliance' and y in 'tcsTCSTcs':
    fn(ril,tcs)
if x in 'relianceRELIANCEReliance' and y in 'itcITCItc':
    fn(ril,itc)
if x in 'relianceRELIANCEReliance' and y in 'infosysINFOSYSInfosys':
    fn(ril,infy)

if x in 'hdfcHDFCHdfc' and y in 'relianceRELIANCEReliance':
    fn(hdfc,ril)
if x in 'hdfcHDFCHdfc' and y in 'asian paintsASIAN PAINTSAsian Paints':
    fn(hdfc,ap)
if x in 'hdfcHDFCHdfc' and y in 'itcITCItc':
    fn(hdfc,itc)
if x in 'hdfcHDFCHdfc' and y in 'tcsTCSTcs':
    fn(hdfc,tcs)
if x in 'hdfcHDFCHdfc' and y in 'infosysINFOSYSInfosys':
    fn(hdfc,infy)

if x in 'infosysINFOSYSInfosys' and y in 'asian paintsASIAN PAINTSAsian Paints':
    fn(infy,ap)
if x in 'infosysINFOSYSInfosys' and y in 'relianceRELIANCEReliance':
    fn(infy,ril)
if x in 'infosysINFOSYSInfosys' and y in 'itcITCItc':
    fn(infy,itc)
if x in 'infosysINFOSYSInfosys' and y in 'tcsTCSTcs':
    fn(infy,tcs)
if x in 'infosysINFOSYSInfosys' and y in 'hdfcHDFCHdfc':
    fn(infy,hdfc)

if x in 'itcITCItc' and y in 'asian paintsASIAN PAINTSAsian Paints':
    fn(itc,ap)
if x in 'itcITCItc' and y in 'relianceRELIANCEReliance':
    fn(itc,ril)
if x in 'itcITCItc' and y in 'tcsTCSTcs':
    fn(itc,tcs)
if x in 'itcITCItc' and y in 'hdfcHDFCHdfc':
    fn(itc,hdfc)
if x in 'itcITCItc' and y in 'infosysINFOSYSInfosys':
    fn(itc,infy)

if x in 'asian paintsASIAN PAINTSAsian Paints' and y in 'itcITCItc':
    fn(ap,itc)
if x in 'asian paintsASIAN PAINTSAsian Paints' and y in 'relianceRELIANCEReliance':
    fn(ap,ril)
if x in 'asian paintsASIAN PAINTSAsian Paints' and y in 'tcsTCSTcs':
    fn(ap,tcs)
if x in 'asian paintsASIAN PAINTSAsian Paints' and y in 'hdfcHDFCHdfc':
    fn(ap,hdfc)
if x in 'asian paintsASIAN PAINTSAsian Paints' and y in 'infosysINFOSYSInfosys':
    fn(ap,infy)

if x in 'tcsTCSTcs' and y in 'itcITCItc':
    fn(tcs,itc)
if x in 'tcsTCSTcs' and y in 'relianceRELIANCEReliance':
    fn(tcs,ril)
if x in 'tcsTCSTcs' and y in 'asian paintsASIAN PAINTSAsian Paints':
    fn(tcs,ap)
if x in 'tcsTCSTcs' and y in 'hdfcHDFCHdfc':
    fn(tcs,hdfc)
if x in 'tcsTCSTcs' and y in 'infosysINFOSYSInfosys':
    fn(tcs,infy)