program leap_year
    implicit none
    integer :: year,i,num=0
    print*,"Enter the year :"
    read*,year
    do i=4,year
    if(mod(i,4)==0.and.mod(i,400)==0.or.mod(i,100)/=0)then
        print*,i
        num=num+1
    end if
    end do
    print*,"The total number of leap year is : ",num
end program leap_year
