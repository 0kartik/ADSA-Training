#Algorithm 
#-> B is the set of booking 
# -> A is the set of accepted bookings ( initially empty)
# -> pick b in B with smallest finishing time
# -> add b to A
# -> remove from B all bookings that overlap with b
# -> if B is empty , STOP 


Booking_list=[]
for Inner in range(int(input())):
    Inner_list=list(map(int,input().split()))
    Booking_list.append(Inner_list)
print(Booking_list)
Selected_shows=[]
Booking_list.sort(key=lambda x:x[1])
last_finished=-1
for Finished in range(len(Booking_list)):
    if Booking_list[Finished][0]>=last_finished:
        Selected_shows.append(Booking_list[Finished])
        last_finished=Booking_list[Finished][1]
print(Selected_shows)
print(len(Selected_shows))