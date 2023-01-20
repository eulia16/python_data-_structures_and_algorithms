#make __contains__ method more efficient(full code on that dudes github repo)

'''Rest of class definition/method shit'''

def __contains__(self, num):
    if self._step == 1:#if step equals 1, just see if number is between min and max of range
        if self._start <= num < self._stop:
            return True;
        else:
            return False;
    else:#if step is not 1, must use modulo to see if remainder is 0
        if self._start <= num < self._stop:
            if (num - self._start) % self._step == 0:
                return True;
            else:
                return False;



 


