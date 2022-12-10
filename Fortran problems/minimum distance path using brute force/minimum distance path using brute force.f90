
program a6q7
    implicit none
    integer,parameter::inf=9999
    integer::array(6),distance_array(5,5),i,counter,total_distance,j,min_distance,min_distance_array(6,inf),min_distance_count
    counter=0
    min_distance_count=0
    min_distance=inf

    do i=1,6  ! here the alphabets a,b,c,d,e are defined to be numerical values for calculation purposes
        array(i)=i
        end do
    array(6)=array(1)

    open(4,file="in6q7.txt")
    open(5,file="out6q7.txt")
    read(4,4)((distance_array(i,j),j=1,5),i=1,5)
    4 format(5i5)

    call perm(array,distance_array,2,5,total_distance,counter,min_distance,min_distance_array,min_distance_count)


    write(5,1)"there are",counter,"possible circuits from the",5,"vertices complete graph"
    write(5,2)"there are ",counter/2," possible unique circuits from the",5,"vertices complete graph"
    write(5,3)"which has a minimum distance of ",min_distance,"from",min_distance_count,"(inc. rep. circ. )of the array/s"
    write(5,5)((min_distance_array(i,j),j=1,6),i=1,min_distance_count)
    1 format (a10,i3,a34,i3,a25)
    2 format (a10,i3,a34,i3,a25)
    3 format (a33,i3,a9,i3,a34)
    5 format (6i3)
    end program



subroutine swap(a,b)
    implicit none
    integer::a,b,t
    t=a
    a=b
    b=t
end subroutine

 recursive subroutine perm(a,d,l,r,td,c,m_d,m_a,m_dc) ! subroutine to find out all possible permutations of a 1 d array and also extract the minimum distance ,number of same minimum distances and minimum distance circuit/s
    integer,parameter::inf=9999
    integer::a(6),l,r,i,c,d(5,5),td,m_d,m_a(6,inf)
     if(l==r) then
        td=0
        do i=1,5
           td=td+d(a(i),a(i+1)) !calculating the total distance for each circuits
        end do

    if(td<=m_d) then
      if(td<m_d) then
        m_dc=0   ! if the previous minimum distance is larger than the current distance then minimum distance count goes back to 0  (29(1),29(2),20(1),20(2),20(3))
      end if

      m_d=td   ! if the previous minimum distance is larger than the current distance then the current distance becomes the new minimum distance


      if(td==m_d)then
        m_dc=m_dc+1  ! counting the minimum distance circuits with the same minimum distances
        do i=1,6
         m_a(m_dc,i)=a(i) !collecting the different circuits with the same minimum distances
        end do
      end if
    end if

        write(5,1)(a(i),i=1,6)," with a total distance of ",td
        1 format(6i3,a28,i3)
        c=c+1  !counting the number of circuits

     else
        do i=l,r
            call swap(a(l),a(i)) ! swap l_th term with the i_th term (abcdea->adcbea(swapped 2nd term with the 4th term))
            call perm(a,d,l+1,r,td,c,m_d,m_a,m_dc)   ! go to the next state fixing position of a certain group and continue(in adcbea:ad is kept fixed as mentioned to be permuted from l+1 )
            call swap(a(l),a(i)) !return to previous state (adcbea->abcdea)
        end do
     end if


end subroutine


