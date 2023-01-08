program t
    implicit none
    integer::a(99,99),det
    integer::i,j,n
!bleh
 n=5

    do i=1,n
        do j=1,n
            read*,a(i,j)
        end do
    end do
write(*,*)det(a,n)
    end program
subroutine cofactor(a,h,n,i,j)
implicit none

integer::a(99,99),h(99,99)
integer::i,j,n,x,y,c,d
c=0
d=0
     do x=1,n
           if(x/=i) then
            c=c+1
            d=0
            do y=1,n
                if(y/=j) then
                d=d+1
              h(c,d)=a(x,y)
                end if
            end do
           end if
        end do
end subroutine

integer recursive function det(a,n) result(t)
implicit none

integer::a(99,99),h(99,99)
integer::i,j,n,f
t=0

If(n==2)then
t=a(2,2)*a(1,1)-a(1,2)*a(2,1)
else
do f=1,n
       call cofactor(a,h,n,1,f)
 t=t+((-1)**(1+f))*a(1,f)*det(h,n-1)
end do
end if

end function det

