program mat_mutiply
    implicit none
    integer::i,j,k,s
    integer,dimension(3,3)::A,B,C
    
    write(*,*)"Enter the entries of the first matrix"
    READ(*,*)((A(i,j),j=1,3),i=1,3)
    write(*,*)"Enter the entries of the second matrix"
    READ(*,*)((B(i,j),j=1,3),i=1,3)
    
    write(*,*)"The first matrix is"
    do i = 1,3
        do j = 1,3
        
         write(*, '( 5x i2 )', Advance = 'No' )A(i,j)
        
        end do
       ! write(*, '( 3x i1 )', Advance = 'No' )i
        write(*,*)""
     end do
     write(*,*)"The second matrix is"
     do i = 1,3
         do j = 1,3
         
          write(*, '( 5x i2 )', Advance = 'No' )B(i,j)
         
         end do
        ! write(*, '( 3x i1 )', Advance = 'No' )i
         write(*,*)""
      end do

    do i = 1,3
        do j = 1,3
            do k = 1,3
            C(i,j) =C(i,j)+ A(i,k)*B(k,j)
            end do
        end do
    end do

    write(*,*)"The final matrix is"
    do i = 1,3
        do j = 1,3
        
         write(*,'(5x i4)', Advance = 'No')C(i,j)
        
        end do
       ! write(*, '( 3x i1 )', Advance = 'No' )i
        write(*,*)""
     end do

    !write(*,*)"The sum is ",s

    end program mat_multiply
