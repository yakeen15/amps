program pattern_print
    implicit none
  
    integer::y,z,i,j,t,l=3
    character(len=3)::obj="*"
    do i = 1,3
       do j = 1,3
        z=(l*j)-1
        do t = 1,z
          write(*, '( a3 )', Advance = 'No' )" "
        end do
        write(*, '( a3 )', Advance = 'No' )obj
       end do
       l=l-1
       write(*,*)""
    end do 
  
  !  *     *        *
  ! *   *     *
  !* *  *
  end program fortran_cdi2

