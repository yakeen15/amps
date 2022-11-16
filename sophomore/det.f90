program fortran_cdi

    implicit none
    integer::i,j,k,s,p,q
    integer,dimension(3,3)::A
    write(*,*)"Enter the entries of the first matrix"
    READ(*,*)((A(i,j),j=1,3),i=1,3)
    
    write(*,*)"The matrix is"
    do i = 1,3
        do j = 1,3
        
         write(*, '( 6x i3 )', Advance = 'No' )A(i,j)
        
        end do
       ! write(*, '( 3x i1 )', Advance = 'No' )i
        write(*,*)""
     end do
    
    s=0
    do k = 1,3
        p=(mod((k),3))+1
        q=(mod((k+1),3))+1
        s = s + (A(1,k)*((A(2,p)*A(3,q))-(A(2,q)*A(3,p))))
    end do

    write(*,*)"The determinant of the matrix is ",s

end program fortran_cdi