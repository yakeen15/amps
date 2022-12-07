program b2d
    implicit none

    integer :: bin, dec=0, i = 1, tempb, rem

    write(*,*) "Input a binary number"
    read(*,*) bin

    tempb = bin

    do while(tempb/=0)
        rem = mod(tempb,10)
        dec = dec + rem*i
        i = i*2
        tempb = tempb/10
    end do

    write(*,'(2(a,i0))') "Decimal of ", bin, " is = ", dec
end program
