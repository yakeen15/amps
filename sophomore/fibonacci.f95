program fibonacci
    implicit none
    integer :: sum=0,i=1,j,k=0
    do j=1,20
        print*,sum
        k=i
        i=sum
        sum=k+i   
    end do
end program fibonacci