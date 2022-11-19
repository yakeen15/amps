PROGRAM  LowestCommonMultiple
    IMPLICIT  NONE
 
    INTEGER   ::x,y, GCD, ans
    
 WRITE(*,*) 'Two positive integers please --> '
    READ(*,*)  x, y
    LCM=(x*y)/(GCD(x,y))
    WRITE(*,*) 'The GCD is ', GCD(x,y)
    WRITE(*,*) 'The LCM is ', LCM

 
 END PROGRAM  LowestCommonMultiple

 INTEGER FUNCTION GCD(a,b)
 INTEGER   :: a, b, c
    IF (a < b) THEN       ! since a >= b must be true, they
       c = a              ! are swapped if a < b
       a = b
       b = c
    END IF
 
    DO                    ! now we have a <= b
       c = MOD(a, b)      !    compute c, the reminder
       IF (c == 0) EXIT   !    if c is zero, we are done.  GCD = b
       a = b              !    otherwise, b becomes a
       b = c              !    and c becomes b
    END DO                !    go back
 
    GCD = b

    
end function
