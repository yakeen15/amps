program fortran_cdi
    implicit none
    integer::i,j,k,p,q,det
    integer,dimension(3,3)::A,cof
    real,dimension(3,3)::inv,temp
    
    write(*,*)"Enter the entries of the first matrix"
    READ(*,*)((A(i,j),j=1,3),i=1,3)
    
    write(*,*)"The matrix is"

    do i = 1,3
        do j = 1,3
        
         write(*, '( 6x i3 )', Advance = 'No' )A(i,j)
        
        end do

        write(*,*)""

     end do
    
    det=0
    do j = 1,3
        p=(mod((j),3))+1
        q=(mod((j+1),3))+1
        det = det + (A(1,j)*((A(2,p)*A(3,q))-(A(2,q)*A(3,p))))
    end do

    write(*,*)"The determinant of the matrix is ",det

    do j = 1,3
        p=(mod((j),3))+1
        q=(mod((j+1),3))+1
        cof(1,j) =  ((A(2,p)*A(3,q))-(A(2,q)*A(3,p)))
    end do

    do j = 1,3
        p=(mod((j),3))+1
        q=(mod((j+1),3))+1
        cof(2,j) =  (-1)*((A(1,p)*A(3,q))-(A(1,q)*A(3,p)))
    end do

    do j = 1,3
        p=(mod((j),3))+1
        q=(mod((j+1),3))+1
        cof(3,j) =  ((A(1,p)*A(2,q))-(A(1,q)*A(2,p)))
    end do

    write(*,*)"The cofactor matrix is"

    do i = 1,3
        do j = 1,3
        
         write(*, '( 6x i4 )', Advance = 'No' )cof(i,j)
        
        end do

        write(*,*)""

     end do

     do i = 1,3
        do j = 1,3
        
         temp(i,j) = REAL(cof(j,i))
        
        end do
     end do

     do i = 1,3
        do j = 1,3
        
         inv(i,j) = (temp(i,j))/det
        
        end do
     end do

    write(*,*)"The inverse matrix is"
    do i = 1,3
        do j = 1,3
        
         write(*, '( 10x f6.2 )', Advance = 'No' )inv(i,j)
        
        end do
       
        write(*,*)""
     end do

    end program fortran_cdi