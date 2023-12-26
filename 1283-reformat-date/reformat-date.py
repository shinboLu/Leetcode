class Solution:
    def reformatDate(self, date: str) -> str:
        month_map =  {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}

        date_list = date.split(' ')

        year = str(date_list[2])
        month = month_map[date_list[1]]
        date_str = ''

        for ch in date_list[0]:
            if ch.isnumeric():
                date_str += ch

        if len(date_str) == 1:
            date_str= '0' + date_str


        return year+'-'+month+'-'+date_str
            

        