fourcc = cv.VideoWriter_fourcc(*'XVID')
videorec = cv.VideoWriter('Record1.mp4',fourcc,20,(640,480))    
videorec.write(frame)