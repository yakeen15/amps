
double precision function det2(a) result(t) ! determinant function  only for a 2x2 matrix
        implicit none
        double precision::a(999)
        t=a(4)*a(1)-a(2)*a(3)
end function det2
double precision  function det3(b) result(t) !determinant function only for a 3x3 matrix
 implicit none
        double precision ::b(999,999)
t=b(1,1)*(b(2,2)*b(3,3)-b(2,3)*b(3,2)) &
         -b(1,2)*(b(2,1)*b(3,3)-b(2,3)*b(3,1)) &
         +b(1,3)*(b(2,1)*b(3,2)-b(3,1)*b(2,2))
end function det3
program q4
     implicit none
     integer,parameter::inf=999
     integer::i,j,v,w,x
      double precision :: Cf(inf,inf),A(inf,inf),M(inf,inf),t(inf),det2,det3,INV_A(inf,inf),adj(inf,inf)
      open(1,file="in3q4.txt")
      open(2,file="out3q4.txt")
read(1,1)((A(i,j),j=1,3),i=1,3)
1 format(3f5.0)

    !formation of minor matrix
x=1
do i=1,3
    do j=1,3
        x=1
               do w=1,3
                  do v=1,3
                     if(w/=i .AND. v/=j) then
                        t(x)=A(w,v)
                        x=x+1
                     end if
                  end do
               end do
 M(i,j)=det2(t)
    end do
end do
   !formation of cofactor matrix
   do i=1,3
    do j=1,3
        Cf(i,j)=((-1)**(i+j))*M(i,j)
    end do
    end do
    !formation of adjoint matrix
   do i=1,3
    do j=1,3
        adj(i,j)=Cf(j,i)
    end do
    end do

!formation of inverse matrix
if(det3(A)==0) then
    Print*,"Determinant is zero so inverse does not exist"
else
   do i=1,3
      do j=1,3
        Inv_A(i,j)=adj(i,j)/det3(A)
      end do
   end do
   write(2,*)"The inverse matrix is:"
   write(2,8)((Inv_A(i,j),j=1,3),i=1,3)
   8 format (3f11.2)
end if

end program


