from tkinter import *
from tkinter.messagebox import askyesno
import tkinter.messagebox as mbox
import webbrowser
from PIL import ImageTk, Image
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from nltk import word_tokenize
from nltk.corpus import stopwords
import mysql.connector
import openpyxl
import os
import time

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user='root',
    password = '',
    database = 'qlbh'
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM vanban ORDER BY mavb ASC")
myresult = mycursor.fetchall()

input_excel = [['Mã văn bản','Tên văn bản','Nội dung văn bản','Tác giả','Tỉ lệ trùng khớp']]

#từ dừng trong tiếng việt (dùng để xử lý ngôn ngữ tự nhiên)
tudung = ['a lô','a ha','ai','ai ai','ai nấy','ai đó','alô','amen','anh','anh ấy','ba','ba ba','ba bản','ba cùng','ba họ','ba ngày','ba ngôi','ba tăng','bao giờ','bao lâu','bao nhiêu','bao nả','bay biến','biết','biết bao','biết bao nhiêu','biết chắc',
'biết chừng nào','biết mình','biết mấy','biết thế','biết trước','biết việc','biết đâu','biết đâu chừng',
'biết đâu đấy','biết được','buổi','buổi làm','buổi mới','buổi ngày','buổi sớm','bà','bà ấy','bài','bài bác','bài bỏ','bài cái','bác',
'bán','bán cấp','bán dạ','bán thế','bây bẩy','bây chừ','bây giờ','bây nhiêu','bèn','béng','bên',
'bên bị','bên có','bên cạnh','bông','bước','bước khỏi','bước tới','bước đi','bạn','bản','bản bộ','bản riêng','bản thân','bản ý','bất chợt','bất cứ','bất giác','bất kì','bất kể','bất kỳ','bất luận','bất ngờ','bất nhược','bất quá','bất quá chỉ','bất thình lình','bất tử','bất đồ',
'bấy','bấy chầy','bấy chừ','bấy giờ','bấy lâu','bấy lâu nay','bấy nay','bấy nhiêu','bập bà bập bõm','bập bõm','bắt đầu','bắt đầu từ','bằng','bằng cứ','bằng không','bằng người','bằng nhau','bằng như',
'bằng nào','bằng nấy','bằng vào','bằng được','bằng ấy','bển','bệt','bị','bị chú','bị vì','bỏ','bỏ bà','bỏ cha','bỏ cuộc','bỏ không','bỏ lại',
'bỏ mình','bỏ mất','bỏ mẹ','bỏ nhỏ','bỏ quá','bỏ ra','bỏ riêng','bỏ việc','bỏ xa','bỗng','bỗng chốc','bỗng dưng','bỗng không',
'bỗng nhiên','bỗng nhưng','bỗng thấy','bỗng đâu','bộ','bộ thuộc','bộ điều','bội phần','bớ','bởi','bởi ai','bởi chưng','bởi nhưng','bởi sao','bởi thế','bởi thế cho nên','bởi tại','bởi vì','bởi vậy',
'bởi đâu','bức','cao','cao lâu','cao ráo','cao răng','cao sang','cao số','cao thấp','cao thế','cao xa','cha','cha chả','chao ôi','chia sẻ','chiếc','cho','cho biết','cho chắc','cho hay','cho nhau','cho nên','cho rằng','cho rồi','cho thấy',
'cho tin','cho tới','cho tới khi','cho về','cho ăn','cho đang','cho được','cho đến','cho đến khi','cho đến nỗi','choa','chu cha','chui cha','chung','chung cho',
'chung chung','chung cuộc','chung cục','chung nhau','chung qui','chung quy','chung quy lại','chung ái','chuyển','chuyển tự','chuyển đạt','chuyện','chuẩn bị','chành chạnh','chí chết','chính','chính bản','chính giữa','chính là','chính thị','chính điểm','chùn chùn','chùn chũn','chú','chú dẫn','chú khách','chú mày','chú mình','chúng','chúng mình','chúng ta','chúng tôi','chúng ông','chăn chắn','chăng','chăng chắc','chăng nữa','chơi','chơi họ','chưa',
'chưa bao giờ','chưa chắc','chưa có','chưa cần','chưa dùng','chưa dễ',
'chưa kể','chưa tính',
'chưa từng','chầm chập',
'chậc','chắc','chắc chắn',
'chắc dạ','chắc hẳn','chắc lòng',
'chắc người','chắc vào','chắc ăn',
'chẳng lẽ','chẳng những','chẳng nữa',
'chẳng phải','chết nỗi','chết thật',
'chết tiệt','chỉ','chỉ chính',
'chỉ có','chỉ là','chỉ tên',
'chỉn','chị','chị bộ','chị ấy',
'chịu','chịu chưa','chịu lời','chịu tốt',
'chịu ăn','chọn','chọn bên','chọn ra',
'chốc chốc','chớ','chớ chi','chớ gì',
'chớ không','chớ kể','chớ như','chợt','chợt nghe',
'chợt nhìn','chủn','chứ','chứ ai','chứ còn','chứ gì',
'chứ không','chứ không phải','chứ lại','chứ lị',
'chứ như','chứ sao','coi bộ','coi mòi','con',
'con con','con dạ','con nhà','con tính','cu cậu','cuối','cuối cùng','cuối điểm','cuốn','cuộc',
'càng','càng càng','càng hay','cá nhân','các','các cậu','cách','cách bức','cách không','cách nhau',
'cách đều','cái',
'cái gì','cái họ','cái đã',
'cái đó',
'cái ấy',
'câu hỏi',
'cây',
'cây nước',
'còn',
'còn như',
'còn nữa',
'còn thời gian',
'còn về',
'có',
'có ai',
'có chuyện',
'có chăng',
'có chăng là',
'có chứ',
'có cơ',
'có dễ',
'có họ',
'có khi',
'có ngày',
'có người',
'có nhiều',
'có nhà',
'có phải',
'có số',
'có tháng',
'có thế',
'có thể',
'có vẻ',
'có ý',
'có ăn',
'có điều',
'có điều kiện',
'có đáng',
'có đâu',
'có được',
'cóc khô',
'cô',
'cô mình',
'cô quả',
'cô tăng',
'cô ấy',
'công nhiên',
'cùng',
'cùng chung',
'cùng cực',
'cùng nhau',
'cùng tuổi',
'cùng tột',
'cùng với',
'cùng ăn',
'căn',
'căn cái',
'căn cắt',
'căn tính',
'cũng',
'cũng như',
'cũng nên',
'cũng thế',
'cũng vậy',
'cũng vậy thôi',
'cũng được',
'cơ',
'cơ chỉ',
'cơ chừng',
'cơ cùng',
'cơ dẫn',
'cơ hồ',
'cơ hội',
'cơ mà',
'cơn',
'cả',
'cả nghe',
'cả nghĩ',
'cả ngày',
'cả người',
'cả nhà',
'cả năm',
'cả thảy',
'cả thể',
'cả tin',
'cả ăn',
'cả đến',
'cảm thấy',
'cảm ơn',
'cấp',
'cấp số',
'cấp trực tiếp',
'cần',
'cần cấp',
'cần gì',
'cần số',
'cật lực',
'cật sức',
'cậu',
'cổ lai',
'cụ thể',
'cụ thể là',
'cụ thể như',
'của',
'của ngọt',
'của tin',
'cứ',
'cứ như',
'cứ việc',
'cứ điểm',
'cực lực',
'do',
'do vì',
'do vậy',
'do đó',
'duy',
'duy chỉ',
'duy có',
'dài',
'dài lời',
'dài ra',
'dành',
'dành dành',
'dào',
'dì',
'dù',
'dù cho',
'dù dì',
'dù gì',
'dù rằng',
'dù sao',
'dùng',
'dùng cho',
'dùng hết',
'dùng làm',
'dùng đến',
'dưới',
'dưới nước',
'dạ',
'dạ bán',
'dạ con',
'dạ dài',
'dạ dạ',
'dạ khách',
'dần dà',
'dần dần',
'dầu sao',
'dẫn',
'dẫu',
'dẫu mà',
'dẫu rằng',
'dẫu sao',
'dễ',
'dễ dùng',
'dễ gì',
'dễ khiến',
'dễ nghe',
'dễ ngươi',
'dễ như chơi',
'dễ sợ',
'dễ sử dụng',
'dễ thường',
'dễ thấy',
'dễ ăn',
'dễ đâu',
'dở chừng',
'dữ',
'dữ cách',
'em',
'em em',
'giá trị',
'giá trị thực tế',
'giảm',
'giảm chính',
'giảm thấp',
'giảm thế',
'giống',
'giống người',
'giống nhau',
'giống như',
'giờ',
'giờ lâu',
'giờ này',
'giờ đi',
'giờ đây',
'giờ đến',
'giữ',
'giữ lấy',
'giữ ý',
'giữa',
'giữa lúc',
'gây',
'gây cho',
'gây giống',
'gây ra',
'gây thêm',
'gì',
'gì gì',
'gì đó',
'gần',
'gần bên',
'gần hết',
'gần ngày',
'gần như',
'gần xa',
'gần đây',
'gần đến',
'gặp',
'gặp khó khăn',
'gặp phải',
'gồm',
'hay',
'hay biết',
'hay hay',
'hay không',
'hay là',
'hay làm',
'hay nhỉ',
'hay nói',
'hay sao',
'hay tin',
'hay đâu',
'hiểu',
'hiện nay',
'hiện tại',
'hoàn toàn',
'hoặc',
'hoặc là',
'hãy',
'hãy còn',
'hơn',
'hơn cả',
'hơn hết',
'hơn là',
'hơn nữa',
'hơn trước',
'hầu hết',
'hết',
'hết chuyện',
'hết cả',
'hết của',
'hết nói',
'hết ráo',
'hết rồi',
'hết ý',
'họ',
'họ gần',
'họ xa',
'hỏi',
'hỏi lại',
'hỏi xem',
'hỏi xin',
'hỗ trợ',
'khi',
'khi khác',
'khi không',
'khi nào',
'khi nên',
'khi trước',
'khiến',
'khoảng',
'khoảng cách',
'khoảng không',
'khá',
'khá tốt',
'khác',
'khác gì',
'khác khác',
'khác nhau',
'khác nào',
'khác thường',
'khác xa',
'khách',
'khó',
'khó biết',
'khó chơi',
'khó khăn',
'khó làm',
'khó mở',
'khó nghe',
'khó nghĩ',
'khó nói',
'khó thấy',
'khó tránh',
'không',
'không ai',
'không bao giờ',
'không bao lâu',
'không biết',
'không bán',
'không chỉ',
'không còn',
'không có',
'không có gì',
'không cùng',
'không cần',
'không cứ',
'không dùng',
'không gì',
'không hay',
'không khỏi',
'không kể',
'không ngoài',
'không nhận',
'không những',
'không phải',
'không phải không',
'không thể',
'không tính',
'không điều kiện',
'không được',
'không đầy',
'không để',
'khẳng định',
'khỏi',
'khỏi nói',
'kể',
'kể cả',
'kể như',
'kể tới',
'kể từ',
'liên quan',
'loại',
'loại từ',
'luôn',
'luôn cả',
'luôn luôn',
'luôn tay',
'là',
'là cùng',
'là là',
'là nhiều',
'là phải',
'là thế nào',
'là vì',
'là ít',
'làm',
'làm bằng',
'làm cho',
'làm dần dần',
'làm gì',
'làm lòng',
'làm lại',
'làm lấy',
'làm mất',
'làm ngay',
'làm như',
'làm nên',
'làm ra',
'làm riêng',
'làm sao',
'làm theo',
'làm thế nào',
'làm tin',
'làm tôi',
'làm tăng',
'làm tại',
'làm tắp lự',
'làm vì',
'làm đúng',
'làm được',
'lâu',
'lâu các',
'lâu lâu',
'lâu nay',
'lâu ngày',
'lên',
'lên cao',
'lên cơn',
'lên mạnh',
'lên ngôi',
'lên nước',
'lên số',
'lên xuống',
'lên đến',
'lòng',
'lòng không',
'lúc',
'lúc khác',
'lúc lâu',
'lúc nào',
'lúc này',
'lúc sáng',
'lúc trước',
'lúc đi',
'lúc đó',
'lúc đến',
'lúc ấy',
'lý do',
'lượng',
'lượng cả',
'lượng số',
'lượng từ',
'lại',
'lại bộ',
'lại cái',
'lại còn',
'lại giống',
'lại làm',
'lại người',
'lại nói',
'lại nữa',
'lại quả',
'lại thôi',
'lại ăn',
'lại đây',
'lấy',
'lấy có',
'lấy cả',
'lấy giống',
'lấy làm',
'lấy lý do',
'lấy lại',
'lấy ra',
'lấy ráo',
'lấy sau',
'lấy số',
'lấy thêm',
'lấy thế',
'lấy vào',
'lấy xuống',
'lấy được',
'lấy để',
'lần',
'lần khác',
'lần lần',
'lần nào',
'lần này',
'lần sang',
'lần sau',
'lần theo',
'lần trước',
'lần tìm',
'lớn',
'lớn lên',
'lớn nhỏ',
'lời',
'lời chú',
'lời nói',
'mang',
'mang lại',
'mang mang',
'mang nặng',
'mang về',
'muốn',
'mà',
'mà cả',
'mà không',
'mà lại',
'mà thôi',
'mà vẫn',
'mình',
'mạnh',
'mất',
'mất còn',
'mọi',
'mọi giờ',
'mọi khi',
'mọi lúc',
'mọi người',
'mọi nơi',
'mọi sự',
'mọi thứ',
'mọi việc',
'mối',
'mỗi',
'mỗi lúc',
'mỗi lần',
'mỗi một',
'mỗi ngày',
'mỗi người',
'một',
'một cách',
'một cơn',
'một khi',
'một lúc',
'một số',
'một vài',
'một ít',
'mới',
'mới hay',
'mới rồi',
'mới đây',
'mở',
'mở mang',
'mở nước',
'mở ra',
'mợ',
'mức',
'nay',
'ngay',
'ngay bây giờ',
'ngay cả',
'ngay khi',
'ngay khi đến',
'ngay lúc',
'ngay lúc này',
'ngay lập tức',
'ngay thật',
'ngay tức khắc',
'ngay tức thì',
'ngay từ',
'nghe',
'nghe chừng',
'nghe hiểu',
'nghe không',
'nghe lại',
'nghe nhìn',
'nghe như',
'nghe nói',
'nghe ra',
'nghe rõ',
'nghe thấy',
'nghe tin',
'nghe trực tiếp',
'nghe đâu',
'nghe đâu như',
'nghe được',
'nghen',
'nghiễm nhiên',
'nghĩ',
'nghĩ lại',
'nghĩ ra',
'nghĩ tới',
'nghĩ xa',
'nghĩ đến',
'nghỉm',
'ngoài',
'ngoài này',
'ngoài ra',
'ngoài xa',
'ngoải',
'nguồn',
'ngày',
'ngày càng',
'ngày cấp',
'ngày giờ',
'ngày ngày',
'ngày nào',
'ngày này',
'ngày nọ',
'ngày qua',
'ngày rày',
'ngày tháng',
'ngày xưa',
'ngày xửa',
'ngày đến',
'ngày ấy',
'ngôi',
'ngôi nhà',
'ngôi thứ',
'ngõ hầu',
'ngăn ngắt',
'ngươi',
'người',
'người hỏi',
'người khác',
'người khách',
'người mình',
'người nghe',
'người người',
'người nhận',
'ngọn',
'ngọn nguồn',
'ngọt',
'ngồi',
'ngồi bệt',
'ngồi không',
'ngồi sau',
'ngồi trệt',
'ngộ nhỡ',
'nhanh',
'nhanh lên',
'nhanh tay',
'nhau',
'nhiên hậu',
'nhiều',
'nhiều ít',
'nhiệt liệt',
'nhung nhăng',
'nhà',
'nhà chung',
'nhà khó',
'nhà làm',
'nhà ngoài',
'nhà ngươi',
'nhà tôi',
'nhà việc',
'nhân dịp',
'nhân tiện',
'nhé',
'nhìn',
'nhìn chung',
'nhìn lại',
'nhìn nhận',
'nhìn theo',
'nhìn thấy',
'nhìn xuống',
'nhóm',
'nhón nhén',
'như',
'như ai',
'như chơi',
'như không',
'như là',
'như nhau',
'như quả',
'như sau',
'như thường',
'như thế',
'như thế nào',
'như thể',
'như trên',
'như trước',
'như tuồng',
'như vậy',
'như ý',
'nhưng',
'nhưng mà',
'nhược bằng',
'nhất',
'nhất loạt',
'nhất luật',
'nhất là',
'nhất mực',
'nhất nhất',
'nhất quyết',
'nhất sinh',
'nhất thiết',
'nhất thì',
'nhất tâm',
'nhất tề',
'nhất đán',
'nhất định',
'nhận',
'nhận biết',
'nhận họ',
'nhận làm',
'nhận nhau',
'nhận ra',
'nhận thấy',
'nhận việc',
'nhận được',
'nhằm',
'nhằm khi',
'nhằm lúc',
'nhằm vào',
'nhằm để',
'nhỉ',
'nhỏ',
'nhỏ người',
'nhớ',
'nhớ bập bõm',
'nhớ lại',
'nhớ lấy',
'nhớ ra',
'nhờ',
'nhờ chuyển',
'nhờ có',
'nhờ nhờ',
'nhờ đó',
'nhỡ ra',
'những',
'những ai',
'những khi',
'những là',
'những lúc',
'những muốn',
'những như',
'nào',
'nào cũng',
'nào hay',
'nào là',
'nào phải',
'nào đâu',
'nào đó',
'này',
'này nọ',
'nên',
'nên chi',
'nên chăng',
'nên làm',
'nên người',
'nên tránh',
'nó',
'nóc',
'nói',
'nói bông',
'nói chung',
'nói khó',
'nói là',
'nói lên',
'nói lại',
'nói nhỏ',
'nói phải',
'nói qua',
'nói ra',
'nói riêng',
'nói rõ',
'nói thêm',
'nói thật',
'nói toẹt',
'nói trước',
'nói tốt',
'nói với',
'nói xa',
'nói ý',
'nói đến',
'nói đủ',
'năm',
'năm tháng',
'nơi',
'nơi nơi',
'nước',
'nước bài',
'nước cùng',
'nước lên',
'nước nặng',
'nước quả',
'nước xuống',
'nước ăn',
'nước đến',
'nấy',
'nặng',
'nặng căn',
'nặng mình',
'nặng về',
'nếu',
'nếu có',
'nếu cần',
'nếu không',
'nếu mà',
'nếu như',
'nếu thế',
'nếu vậy',
'nếu được',
'nền',
'nọ',
'nớ',
'nức nở',
'nữa',
'nữa khi',
'nữa là',
'nữa rồi',
'oai oái',
'oái',
'pho',
'phè',
'phè phè',
'phía',
'phía bên',
'phía bạn',
'phía dưới',
'phía sau',
'phía trong',
'phía trên',
'phía trước',
'phóc',
'phót',
'phù hợp',
'phăn phắt',
'phương chi',
'phải',
'phải biết',
'phải chi',
'phải chăng',
'phải cách',
'phải cái'
'phải giờ',
'phải khi',
'phải không',
'phải lại',
'phải lời',
'phải người',
'phải như',
'phải rồi',
'phải tay',
'phần',
'phần lớn',
'phần nhiều',
'phần nào',
'phần sau',
'phần việc',
'phắt',
'phỉ phui',
'phỏng',
'phỏng như',
'phỏng nước',
'phỏng theo',
'phỏng tính',
'phốc',
'phụt',
'phứt',
'qua',
'qua chuyện',
'qua khỏi',
'qua lại',
'qua lần',
'qua ngày',
'qua tay',
'qua thì',
'qua đi',
'quan trọng',
'quan trọng vấn đề',
'quan tâm',
'quay',
'quay bước',
'quay lại',
'quay số',
'quay đi',
'quá',
'quá bán',
'quá bộ',
'quá giờ',
'quá lời',
'quá mức',
'quá nhiều',
'quá tay',
'quá thì',
'quá tin',
'quá trình',
'quá tuổi',
'quá đáng',
'quá ư',
'quả',
'quả là',
'quả thật',
'quả thế',
'quả vậy',
'quận',
'ra',
'ra bài',
'ra bộ',
'ra chơi',
'ra gì',
'ra lại',
'ra lời',
'ra ngôi',
'ra người',
'ra sao',
'ra tay',
'ra vào',
'ra ý',
'ra điều',
'ra đây',
'ren rén',
'riu ríu',
'riêng',
'riêng từng',
'riệt',
'rày',
'ráo',
'ráo cả',
'ráo nước',
'ráo trọi',
'rén',
'rén bước',
'rích',
'rón rén',
'rõ',
'rõ là',
'rõ thật',
'rút cục',
'răng',
'răng răng',
'rất',
'rất lâu',
'rằng',
'rằng là',
'rốt cuộc',
'rốt cục',
'rồi',
'rồi nữa',
'rồi ra',
'rồi sao',
'rồi sau',
'rồi tay',
'rồi thì',
'rồi xem',
'rồi đây',
'rứa',
'sa sả',
'sang',
'sang năm',
'sang sáng',
'sang tay',
'sao',
'sao bản',
'sao bằng',
'sao cho',
'sao vậy',
'sao đang',
'sau',
'sau chót',
'sau cuối',
'sau cùng',
'sau hết',
'sau này',
'sau nữa',
'sau sau',
'sau đây',
'sau đó',
'so',
'so với',
'song le',
'suýt',
'suýt nữa',
'sáng',
'sáng ngày',
'sáng rõ',
'sáng thế',
'sáng ý',
'sì',
'sì sì',
'sất',
'sắp',
'sắp đặt',
'sẽ',
'sẽ biết',
'sẽ hay',
'số',
'số cho biết',
'số cụ thể',
'số loại',
'số là',
'số người',
'số phần',
'số thiếu',
'sốt sột',
'sớm',
'sớm ngày',
'sở dĩ',
'sử dụng',
'sự',
'sự thế',
'sự việc',
'tanh',
'tanh tanh',
'tay',
'tay quay',
'tha hồ',
'tha hồ chơi',
'tha hồ ăn',
'than ôi',
'thanh',
'thanh ba',
'thanh chuyển',
'thanh không',
'thanh thanh',
'thanh tính',
'thanh điều kiện',
'thanh điểm',
'thay đổi',
'thay đổi tình trạng',
'theo',
'theo bước',
'theo như',
'theo tin',
'thi thoảng',
'thiếu',
'thiếu gì',
'thiếu điểm',
'thoạt',
'thoạt nghe',
'thoạt nhiên',
'thoắt',
'thuần',
'thuần ái',
'thuộc',
'thuộc bài',
'thuộc cách',
'thuộc lại',
'thuộc từ',
'thà',
'thà là',
'thà rằng',
'thành ra',
'thành thử',
'thái quá',
'tháng',
'tháng ngày',
'tháng năm',
'tháng tháng',
'thêm',
'thêm chuyện',
'thêm giờ',
'thêm vào',
'thì',
'thì giờ',
'thì là',
'thì phải',
'thì ra',
'thì thôi',
'thình lình',
'thích',
'thích cứ',
'thích thuộc',
'thích tự',
'thích ý',
'thím',
'thôi',
'hôi việc',
'thúng thắng',
'thương ôi',
'thường',
'thường bị',
'thường hay',
'thường khi',
'thường số',
'thường sự',
'thường thôi',
'thường thường',
'thường tính',
'thường tại',
'thường xuất hiện',
'thường đến',
'thảo hèn',
'thảo nào',
'thấp',
'thấp cơ',
'thấp thỏm',
'thấp xuống',
'thấy',
'thấy tháng',
'thẩy',
'thậm',
'thậm chí',
'thậm cấp',
'thậm từ',
'thật',
'thật chắc',
'thật là',
'thật lực',
'thật quả',
'thật rất',
'thật sự',
'thật thà',
'thật tốt',
'thật vậy',
'thế',
'thế chuẩn bị',
'thế là',
'thế lại',
'thế mà',
'thế nào',
'thế nên',
'thế ra',
'thế sự',
'thế thì',
'thế thôi',
'thế thường',
'thế thế',
'thế à',
'thế đó',
'thếch',
'thỉnh thoảng',
'thỏm',
'thốc',
'thốc tháo',
'thốt',
'thốt nhiên',
'thốt nói',
'thốt thôi',
'thộc',
'thời gian',
'thời gian sử dụng',
'thời gian tính',
'thời điểm',
'thục mạng',
'thứ',
'thứ bản',
'thứ đến',
'thửa',
'thực hiện',
'thực hiện đúng',
'thực ra',
'thực sự',
'thực tế',
'thực vậy',
'tin',
'tin thêm',
'tin vào',
'tiếp theo',
'tiếp tục',
'tiếp đó',
'tiện thể',
'toà',
'toé khói',
'toẹt',
'trong',
'trong khi',
'trong lúc',
'trong mình',
'trong ngoài',
'trong này',
'trong số',
'trong vùng',
'trong đó',
'trong ấy',
'tránh',
'tránh khỏi',
'tránh ra',
'tránh tình trạng',
'tránh xa',
'trên',
'trên bộ',
'trên dưới',
'trước',
'trước hết',
'trước khi',
'trước kia',
'trước nay',
'trước ngày',
'trước nhất',
'trước sau',
'trước tiên',
'trước tuổi',
'trước đây',
'trước đó',
'trả',
'trả của',
'trả lại',
'trả ngay',
'trả trước',
'trếu tráo',
'trển',
'trệt',
'trệu trạo',
'trỏng',
'trời đất ơi',
'trở thành',
'trừ phi',
'trực tiếp',
'trực tiếp làm',
'tuy',
'tuy có',
'tuy là',
'tuy nhiên',
'tuy rằng',
'tuy thế',
'tuy vậy',
'tuy đã',
'tuyệt nhiên',
'tuần tự',
'tuốt luốt',
'tuốt tuồn tuột',
'tuốt tuột',
'tuổi',
'tuổi cả',
'tuổi tôi',
'tà tà',
'tên',
'tên chính',
'tên cái',
'tên họ',
'tên tự',
'tênh',
'tênh tênh',
'tìm',
'tìm bạn',
'tìm cách',
'tìm hiểu',
'tìm ra',
'tìm việc',
'tình trạng',
'tính',
'tính cách',
'tính căn',
'tính người',
'tính phỏng',
'tính từ',
'tít mù',
'tò te',
'tôi',
'tôi con',
'tông tốc',
'tù tì',
'tăm tắp',
'tăng',
'tăng chúng',
'tăng cấp',
'tăng giảm',
'tăng thêm',
'tăng thế',
'tại',
'tại lòng',
'tại nơi',
'tại sao',
'tại tôi',
'tại vì',
'tại đâu',
'tại đây',
'tại đó',
'tạo',
'tạo cơ hội',
'tạo nên',
'tạo ra',
'tạo ý',
'tạo điều kiện',
'tấm',
'tấm bản',
'tấm các',
'tấn',
'tấn tới',
'tất cả',
'tất cả bao nhiêu',
'tất thảy',
'tất tần tật',
'tất tật',
'tập trung',
'tắp',
'tắp lự',
'tắp tắp',
'tọt',
'tỏ ra',
'tỏ vẻ',
'tốc tả',
'tối ư',
'tốt',
'tốt bạn',
'tốt bộ',
'tốt hơn','tốt mối','tốt ngày','tột','tột cùng','tớ','tới','tới gần','tới mức','tới nơi','tới thì','tức thì','tức tốc','từ','từ căn','từ giờ','từ khi','từ loại','từ nay','từ thế','từ tính',
'từ tại','từ từ','từ ái','từ điều','từ đó','từ ấy','từng','từng cái','từng giờ','từng nhà','từng phần',
'từng thời gian',
'từng đơn vị',
'từng ấy',
'tự',
'tự cao',
'tự khi',
'tự lượng',
'tự tính',
'tự tạo',
'tự vì',
'tự ý',
'tự ăn',
'tựu trung',
'veo',
'veo veo',
'việc',
'việc gì',
'vung thiên địa',
'vung tàn tán',
'vung tán tàn',
'và',
'vài',
'vài ba',
'vài người',
'vài nhà',
'vài nơi',
'vài tên',
'vài điều',
'vào',
'vào gặp',
'vào khoảng',
'vào lúc',
'vào vùng',
'vào đến',
'vâng',
'vâng chịu',
'vâng dạ',
'vâng vâng',
'vâng ý',
'vèo',
'vèo vèo',
'vì',
'vì chưng',
'vì rằng',
'vì sao',
'vì thế',
'vì vậy',
'ví bằng',
'ví dù',
'ví phỏng',
'ví thử',
'vô hình trung',
'vô kể',
'vô luận',
'vô vàn',
'vùng',
'vùng lên',
'vùng nước',
'văng tê',
'vượt',
'vượt khỏi',
'vượt quá',
'vạn nhất',
'vả chăng',
'vả lại',
'vấn đề',
'vấn đề quan trọng',
'vẫn',
'vẫn thế',
'vậy',
'vậy là',
'vậy mà',
'vậy nên',
'vậy ra',
'vậy thì',
'vậy ư',
'về',
'về không',
'về nước',
'về phần',
'về sau',
'về tay',
'vị trí',
'vị tất',
'vốn dĩ',
'với',
'với lại',
'với nhau',
'vở',
'vụt',
'vừa',
'vừa khi',
'vừa lúc',
'vừa mới',
'vừa qua',
'vừa rồi',
'vừa vừa',
'xa',
'xa cách',
'xa gần',
'xa nhà',
'xa tanh',
'xa tắp',
'xa xa',
'xa xả',
'xem',
'xem lại',
'xem ra',
'xem số',
'xin',
'xin gặp',
'xin vâng',
'xiết bao',
'xon xón',
'xoành xoạch',
'xoét',
'xoẳn',
'xoẹt',
'xuất hiện',
'xuất kì bất ý',
'xuất kỳ bất ý',
'xuể',
'xuống',
'xăm xúi',
'xăm xăm',
'xăm xắm',
'xảy ra',
'xềnh xệch',
'xệp',
'xử lý',
'yêu cầu',
'à',
'à này',
'à ơi',
'ào',
'ào vào',
'ào ào',
'á',
'á à',
'ái',
'ái chà',
'ái dà',
'áng',
'áng như',
'âu là',
'ít',
'ít biết',
'ít có',
'ít hơn',
'ít khi',
'ít lâu',
'ít nhiều',
'ít nhất',
'ít nữa',
'ít quá',
'ít ra',
'ít thôi',
'ít thấy',
'ô hay',
'ô hô',
'ô kê',
'ô kìa',
'ôi chao',
'ôi thôi',
'ông',
'ông nhỏ',
'ông tạo',
'ông từ',
'ông ấy',
'ông ổng',
'úi',
'úi chà',
'úi dào',
'ý',
'ý chừng',
'ý da',
'ý hoặc',
'ăn',
'ăn chung',
'ăn chắc',
'ăn chịu',
'ăn cuộc',
'ăn hết',
'ăn hỏi',
'ăn làm',
'ăn người',
'ăn ngồi',
'ăn quá',
'ăn riêng',
'ăn sáng',
'ăn tay',
'ăn trên',
'ăn về',
'đang',
'đang tay',
'đang thì',
'điều',
'điều gì',
'điều kiện',
'điểm',
'điểm chính',
'điểm gặp',
'điểm đầu tiên',
'đành đạch',
'đáng',
'đáng kể',
'đáng lí',
'đáng lý',
'đáng lẽ',
'đáng số',
'đánh giá',
'đánh đùng',
'đáo để',
'đâu',
'đâu có',
'đâu cũng',
'đâu như',
'đâu nào',
'đâu phải',
'đâu đâu',
'đâu đây',
'đâu đó',
'đây',
'đây này',
'đây rồi',
'đây đó',
'đã',
'đã hay',
'đã không',
'đã là',
'đã lâu',
'đã thế',
'đã vậy',
'đã đủ',
'đó',
'đó đây',
'đúng',
'đúng ngày',
'đúng ra',
'đúng tuổi',
'đúng với',
'đơn vị',
'đưa',
'đưa cho',
'đưa chuyện',
'đưa em',
'đưa ra',
'đưa tay',
'đưa tin',
'đưa tới','đưa vào','đưa về','đưa xuống','đưa đến','được','được cái','được lời','được nước','được tin','đại loại',
'đại nhân','đại phàm','đại để','đạt','đảm bảo','đầu tiên','đầy','đầy năm',
'đầy phè','đầy tuổi','đặc biệt','đặt','đặt làm','đặt mình','đặt mức','đặt ra','đặt trước','đặt để','đến','đến bao giờ','đến cùng','đến cùng cực','đến cả','đến giờ','đến gần','đến hay','đến khi','đến lúc','đến lời',
'đến nay','đến ngày','đến nơi','đến nỗi','đến thì','đến thế','đến tuổi','đến xem','đến điều','đến đâu','đều','đều bước','đều nhau','đều đều','để','để cho','để giống','để không','để lòng','để lại','để mà','để phần','để được','để đến nỗi','đối với','đồng thời','đủ','đủ dùng','đủ nơi','đủ số','đủ điều','đủ điểm','ơ',
'ơ hay','ơ kìa','ơi','ơi là','ư','ạ','ạ ơi','ấy','ấy là','ầu ơ','ắt','ắt hẳn','ắt là','ắt phải','ắt thật','ối dào','ối giời','ối giời ơi','ồ','ồ ồ','ổng','ớ','ớ này','ờ','ờ ờ','ở','ở lại','ở như','ở nhờ','ở năm','ở trên','ở vào','ở đây','ở đó','ở được','ủa','ứ hự','ứ ừ','ừ','ừ nhé','ừ thì','ừ ào','ừ ừ','ử',]

def open_file1():
    box1.delete(1.0,END)
    text_file = filedialog.askopenfilename(initialdir="This PC:/",title="Open Text",filetypes=(("Text Files","*.txt"),))
    if(str(text_file).__eq__("")):
        mbox.showwarning("Thông báo","Bạn chưa chọn file.")
    else:
        text_file = open(text_file, 'r', encoding='UTF-8')
        stuff = text_file.read()
        if (len(stuff) <= 1):
            mbox.showwarning("Thông báo", "File bạn vừa chọn rỗng!\nVui lòng chọn file khác!")
            text_file.close()
        else:
            box1.insert(END, str(stuff).lstrip().rstrip())
            text_file.close()

def xoa1():
    box1.delete(1.0,END)
    box1.focus()
    btn11.delete(1.0, END)
    btn21.delete(1.0, END)
    btn31.delete(1.0, END)
    btn41.delete(1.0, END)
    btn51.delete(1.0, END)
    txt11.delete(1.0, END)
    txt21.delete(1.0, END)
    txt31.delete(1.0, END)
    txt41.delete(1.0, END)
    txt51.delete(1.0, END)

#hàm kiểm tra trùng lặp văn bản tiếng việt
def kiemtradaovan1(url):
    X = url
    Y = box1.get(1.0, END)
    # mã hóa văn bản
    x_list = word_tokenize(X)
    y_list = word_tokenize(Y)
    # sw chứa danh sách các từ dừng
    # sw = stopwords.words('english')
    sw = tudung
    l1 = []
    l2 = []
    # xóa các từ dừng khỏi chuỗi văn bản
    X_set = {w for w in x_list if not w in sw}
    Y_set = {w for w in y_list if not w in sw}
    # tạo 1 tập hợp chứa các từ khóa của 2 chuỗi
    rvector = X_set.union(Y_set)
    for i in rvector:
        if i in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if i in Y_set:
            l2.append(1)  # create a vector
        else:
            l2.append(0)
        # Công thức cosine
        c = 0
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = (c / float((sum(l1) * sum(l2)) ** 0.5)) * 100
    return round(cosine,2)

def output_Excel(input_detail, output_excel_path):
    # Xác định số hàng và cột lớn nhất trong file excel cần tạo
    row = len(input_detail)
    column = len(input_detail[0])

    # Tạo một workbook mới và active nó
    wb = openpyxl.Workbook()
    ws = wb.active

    # Dùng vòng lặp for để ghi nội dung từ input_detail vào file Excel
    for i in range(0, row):
        for j in range(0, column):
            v = input_detail[i][j]
            ws.cell(column=j + 1, row=i + 1, value=v)

    # Lưu lại file Excel
    wb.save(output_excel_path)

def timkiem1():
    choice = str(variable.get())
    if(choice.__eq__("Internet")):
        if len(box1.get(1.0, END)) <= 50:
            mbox.showwarning("Thông báo!", "Không được để trống hoặc ít hơn 50 ký tự!")
        else:
            # set trạng thái edit
            btn11.config(state=NORMAL)
            btn21.config(state=NORMAL)
            btn31.config(state=NORMAL)
            btn41.config(state=NORMAL)
            btn51.config(state=NORMAL)

            txt11.config(state=NORMAL)
            txt21.config(state=NORMAL)
            txt31.config(state=NORMAL)
            txt41.config(state=NORMAL)
            txt51.config(state=NORMAL)

            btn11.delete(1.0, END)
            btn21.delete(1.0, END)
            btn31.delete(1.0, END)
            btn41.delete(1.0, END)
            btn51.delete(1.0, END)
            txt11.delete(1.0, END)
            txt21.delete(1.0, END)
            txt31.delete(1.0, END)
            txt41.delete(1.0, END)
            txt51.delete(1.0, END)

            chuoi11.delete(1.0, END)
            chuoi21.delete(1.0, END)
            chuoi31.delete(1.0, END)
            chuoi41.delete(1.0, END)
            chuoi51.delete(1.0, END)

            dem = 0
            find = str(box1.get(1.0, END))
            mang_timkiem = find.split(". ")
            count = 0
            for vt in mang_timkiem:
                count += 1
            for i in search(box1.get(1.0, END), stop=5, lang="vn"):
                dem += 1
                url = requests.get(i)
                soup = BeautifulSoup(url.content, "html.parser")
                title = soup.find_all("p")
                tile = 0
                for t in title:
                    if (str(t.text).__contains__(find)):
                        result = str(t.text).lstrip().rstrip()
                        tile = kiemtradaovan1(result)
                        continue
                    else:
                        ketqua = 0
                        mang_title = str(t.text).split(". ")
                        for po in mang_title:
                            for po1 in mang_timkiem:
                                if (po.__contains__(po1)):
                                    ketqua += 1
                        if (ketqua > count / 2):
                            result = str(t.text).lstrip().rstrip()
                            tile = kiemtradaovan1(result)
                if dem == 1:
                    btn11.insert(END, i)
                    txt11.insert(END, tile)
                    if tile == 0:
                        chuoi11.insert(END, "")
                    else:
                        chuoi11.insert(END, result)
                if dem == 2:
                    btn21.insert(END, i)
                    txt21.insert(END, tile)
                    if tile == 0:
                        chuoi21.insert(END, "")
                    else:
                        chuoi21.insert(END, result)
                if dem == 3:
                    btn31.insert(END, i)
                    txt31.insert(END, tile)
                    if tile == 0:
                        chuoi31.insert(END, "")
                    else:
                        chuoi31.insert(END, result)
                if dem == 4:
                    btn41.insert(END, i)
                    txt41.insert(END, tile)
                    if tile == 0:
                        chuoi41.insert(END, "")
                    else:
                        chuoi41.insert(END, result)
                if dem == 5:
                    btn51.insert(END, i)
                    txt51.insert(END, tile)
                    if tile == 0:
                        chuoi51.insert(END, "")
                    else:
                        chuoi51.insert(END, result)
                    # set trạng thái readonly
                    btn11.config(state=DISABLED)
                    btn21.config(state=DISABLED)
                    btn31.config(state=DISABLED)
                    btn41.config(state=DISABLED)
                    btn51.config(state=DISABLED)

                    txt11.config(state=DISABLED)
                    txt21.config(state=DISABLED)
                    txt31.config(state=DISABLED)
                    txt41.config(state=DISABLED)
                    txt51.config(state=DISABLED)

                    mbox.showinfo("Thông báo", "Kết thúc tìm kiếm")
                    kiemtrathienthi1()
    if(choice.__eq__("MySQL")):
        if len(box1.get(1.0, END)) <= 50:
            mbox.showwarning("Thông báo!", "Không được để trống hoặc ít hơn 50 ký tự!")
        else:
            # set trạng thái edit
            btn11.config(state=NORMAL)
            btn21.config(state=NORMAL)
            btn31.config(state=NORMAL)
            btn41.config(state=NORMAL)
            btn51.config(state=NORMAL)

            txt11.config(state=NORMAL)
            txt21.config(state=NORMAL)
            txt31.config(state=NORMAL)
            txt41.config(state=NORMAL)
            txt51.config(state=NORMAL)

            btn11.delete(1.0, END)
            btn21.delete(1.0, END)
            btn31.delete(1.0, END)
            btn41.delete(1.0, END)
            btn51.delete(1.0, END)
            txt11.delete(1.0, END)
            txt21.delete(1.0, END)
            txt31.delete(1.0, END)
            txt41.delete(1.0, END)
            txt51.delete(1.0, END)

            chuoi11.delete(1.0, END)
            chuoi21.delete(1.0, END)
            chuoi31.delete(1.0, END)
            chuoi41.delete(1.0, END)
            chuoi51.delete(1.0, END)
            input_detail = []
            def themsv(a, b, c, d, e):
                hang = len(input_detail) + 1
                input_detail.insert(hang, [a, b, c, d, e])
            for x in myresult:
                dt = str(x[2])
                # print("- Mã văn bản: "+str(x[0]))
                # print("- Tên văn bản: " + str(x[1]))
                # print("- Nội dung văn bản: "+ dt)
                # print("- Tác giả: "+str(x[3]))
                themsv(x[0], x[1], x[2], x[3], kiemtradaovan1(dt))
            #print(input_detail)
            a = sorted(input_detail, key=lambda a_entry: a_entry[4],reverse=True)
            dong = 0
            for i in a:
                dong+=1
                if (dong == 1):
                    btn11.insert(END, str(i[1]))
                    txt11.insert(END, str(i[4])+"%")
                    chuoi11.insert(END, str(i[2]))
                if (dong == 2):
                    btn21.insert(END, str(i[1]))
                    txt21.insert(END, str(i[4])+"%")
                    chuoi21.insert(END, str(i[2]))
                if (dong == 3):
                    btn31.insert(END, str(i[1]))
                    txt31.insert(END, str(i[4])+"%")
                    chuoi31.insert(END, str(i[2]))
                if (dong == 4):
                    btn41.insert(END, str(i[1]))
                    txt41.insert(END, str(i[4])+"%")
                    chuoi41.insert(END, str(i[2]))
                if (dong == 5):
                    btn51.insert(END, str(i[1]))
                    txt51.insert(END, str(i[4])+"%")
                    chuoi51.insert(END, str(i[2]))
                    # set trạng thái readonly
                    btn11.config(state=DISABLED)
                    btn21.config(state=DISABLED)
                    btn31.config(state=DISABLED)
                    btn41.config(state=DISABLED)
                    btn51.config(state=DISABLED)
                    txt11.config(state=DISABLED)
                    txt21.config(state=DISABLED)
                    txt31.config(state=DISABLED)
                    txt41.config(state=DISABLED)
                    txt51.config(state=DISABLED)
                    mbox.showinfo("Thông báo", "Kết thúc tìm kiếm")
                    kiemtrathienthi1()
                    search11.config(state=DISABLED)
                    search21.config(state=DISABLED)
                    search31.config(state=DISABLED)
                    search41.config(state=DISABLED)
                    search51.config(state=DISABLED)
                    save_ex.place(x=600, y=690)
    if(choice.__eq__("Data on Computer")):
        if len(box1.get(1.0, END)) <= 50:
            mbox.showwarning("Thông báo!", "Không được để trống hoặc ít hơn 50 ký tự!")
        else:
            print("Bạn vừa chọn Data on Computer")

#hàm hiển thị kết quả tìm được ra textbox frame1
def hienthiketqua11():
    if len(chuoi11.get(1.0,END)) <= 2:
        mbox.showerror("Thông báo","Không tìm thấy đoạn văn trùng khớp")
    else:
        app1 = Tk()
        app1.title("Đoạn văn trùng khớp")
        app1.geometry("1150x320+400+200")
        app1.resizable(width=FALSE, height=FALSE)
        app1.config(background="grey")

        def save_file():
            if (len(str(txt.get(1.0, END))) <= 2):
                mbox.showerror("Thông báo", "File không được để trống")
            else:
                text_file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
                text_file = open(text_file, 'w', encoding='UTF-8')
                text_file.write(txt.get(1.0, END))
                text_file.close()
                mbox._show("Thông báo!", "Ghi file thành công!")
                txt.delete(1.0, END)

        def quit_app():
            app1.destroy()

        txt = Text(app1, width=100, height=10, font=("Arial", 15), )
        txt.pack(pady=15)
        txt.delete(1.0, END)
        txt.insert(END, chuoi11.get(1.0, END))
        #print(len(str(txt.get(1.0, END))))
        btn_save = Button(app1, text="Save file", bg="yellow", command=save_file, width=10)
        btn_save.place(x=420, y=270)
        btn_quit = Button(app1, text="Exit", bg="red", command=quit_app, width=10)
        btn_quit.place(x=580,y=270)
        app1.mainloop()
def hienthiketqua21():
    if len(chuoi21.get(1.0,END)) <= 2:
        mbox.showerror("Thông báo","Không tìm thấy đoạn văn trùng khớp")
    else:
        app1 = Tk()
        app1.title("Đoạn văn trùng khớp")
        app1.geometry("1150x320+400+200")
        app1.resizable(width=FALSE, height=FALSE)
        app1.config(background="grey")

        def save_file():
            if (len(str(txt.get(1.0, END))) <= 2):
                mbox.showerror("Thông báo", "File không được để trống")
            else:
                text_file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
                text_file = open(text_file, 'w', encoding='UTF-8')
                text_file.write(txt.get(1.0, END))
                text_file.close()
                mbox._show("Thông báo!", "Ghi file thành công!")
                txt.delete(1.0, END)
        def quit_app():
            app1.destroy()
        txt = Text(app1, width=100, height=10, font=("Arial", 15), )
        txt.pack(pady=15)
        txt.delete(1.0, END)
        txt.insert(END, chuoi21.get(1.0, END))
        print(len(str(txt.get(1.0, END))))
        btn_save = Button(app1, text="Save file", bg="yellow", command=save_file, width=10)
        btn_save.place(x=420, y=270)
        btn_quit = Button(app1, text="Exit", bg="red", command=quit_app, width=10)
        btn_quit.place(x=580, y=270)
        app1.mainloop()
def hienthiketqua31():
    if len(chuoi31.get(1.0, END)) <= 2:
        mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
    else:
        app1 = Tk()
        app1.title("Đoạn văn trùng khớp")
        app1.geometry("1150x320+400+200")
        app1.resizable(width=FALSE, height=FALSE)
        app1.config(background="grey")

        def save_file():
            if (len(str(txt.get(1.0, END))) <= 2):
                mbox.showerror("Thông báo", "File không được để trống")
            else:
                text_file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
                text_file = open(text_file, 'w', encoding='UTF-8')
                text_file.write(txt.get(1.0, END))
                text_file.close()
                mbox._show("Thông báo!", "Ghi file thành công!")
                txt.delete(1.0, END)
        def quit_app():
            app1.destroy()
        txt = Text(app1, width=100, height=10, font=("Arial", 15), )
        txt.pack(pady=15)
        txt.delete(1.0, END)
        txt.insert(END, chuoi31.get(1.0, END))
        print(len(str(txt.get(1.0, END))))
        btn_save = Button(app1, text="Save file", bg="yellow", command=save_file, width=10)
        btn_save.place(x=420, y=270)
        btn_quit = Button(app1, text="Exit", bg="red", command=quit_app, width=10)
        btn_quit.place(x=580, y=270)
        app1.mainloop()
def hienthiketqua41():
    if len(chuoi41.get(1.0, END)) <= 2:
        mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
    else:
        app1 = Tk()
        app1.title("Đoạn văn trùng khớp")
        app1.geometry("1150x320+400+200")
        app1.resizable(width=FALSE, height=FALSE)
        app1.config(background="grey")

        def save_file():
            if (len(str(txt.get(1.0, END))) <= 2):
                mbox.showerror("Thông báo", "File không được để trống")
            else:
                text_file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
                text_file = open(text_file, 'w', encoding='UTF-8')
                text_file.write(txt.get(1.0, END))
                text_file.close()
                mbox._show("Thông báo!", "Ghi file thành công!")
                txt.delete(1.0, END)
        def quit_app():
            app1.destroy()
        txt = Text(app1, width=100, height=10, font=("Arial", 15), )
        txt.pack(pady=15)
        txt.delete(1.0, END)
        txt.insert(END, chuoi41.get(1.0, END))
        print(len(str(txt.get(1.0, END))))
        btn_save = Button(app1, text="Save file", bg="yellow", command=save_file, width=10)
        btn_save.place(x=420, y=270)
        btn_quit = Button(app1, text="Exit", bg="red", command=quit_app, width=10)
        btn_quit.place(x=580, y=270)
        app1.mainloop()
def hienthiketqua51():
    if len(chuoi51.get(1.0, END)) <= 2:
        mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
    else:
        app1 = Tk()
        app1.title("Đoạn văn trùng khớp")
        app1.geometry("1150x320+400+200")
        app1.resizable(width=FALSE, height=FALSE)
        app1.config(background="grey")
        def save_file():
            if (len(str(txt.get(1.0, END))) <= 2):
                mbox.showerror("Thông báo", "File không được để trống")
            else:
                text_file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
                text_file = open(text_file, 'w', encoding='UTF-8')
                text_file.write(txt.get(1.0, END))
                text_file.close()
                mbox._show("Thông báo!", "Ghi file thành công!")
                txt.delete(1.0, END)
        def quit_app():
            app1.destroy()

        txt = Text(app1, width=100, height=10, font=("Arial", 15), )
        txt.pack(pady=15)
        txt.delete(1.0,END)
        txt.insert(END, chuoi51.get(1.0, END))
        print(len(str(txt.get(1.0, END))))
        btn_save = Button(app1, text="Save file", bg="yellow", command=save_file, width=10)
        btn_save.place(x=420, y=270)
        btn_quit = Button(app1, text="Exit", bg="red", command=quit_app, width=10)
        btn_quit.place(x=580, y=270)
        app1.mainloop()

#hàm tắt/bật các button frame1
def kiemtrathienthi1():
    if (len(btn11.get(1.0, END)) <= 1):
        show11.config(state=DISABLED)
        search11.config(state=DISABLED)
    else:
        show11.config(state=NORMAL)
        search11.config(state=NORMAL)

    if (len(btn21.get(1.0, END)) <= 1):
        show21.config(state=DISABLED)
        search21.config(state=DISABLED)
    else:
        show21.config(state=NORMAL)
        search21.config(state=NORMAL)

    if (len(btn31.get(1.0, END)) <= 1):
        show31.config(state=DISABLED)
        search31.config(state=DISABLED)
    else:
        show31.config(state=NORMAL)
        search31.config(state=NORMAL)

    if (len(btn41.get(1.0, END)) <= 1):
        show41.config(state=DISABLED)
        search41.config(state=DISABLED)
    else:
        show41.config(state=NORMAL)
        search41.config(state=NORMAL)

    if (len(btn51.get(1.0, END)) <= 1):
        show51.config(state=DISABLED)
        search51.config(state=DISABLED)
    else:
        show51.config(state=NORMAL)
        search51.config(state=NORMAL)
#hàm tra cứu kết quả tìm được
def tracuu11():
    webbrowser.open(btn11.get(1.0,END))
def tracuu21():
    webbrowser.open(btn21.get(1.0,END))
def tracuu31():
    webbrowser.open(btn31.get(1.0,END))
def tracuu41():
    webbrowser.open(btn41.get(1.0,END))
def tracuu51():
    webbrowser.open(btn51.get(1.0,END))

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

root = Tk()
root.title("Hệ Thống Phát Hiện Đạo Văn ( Python )")
root.geometry("1400x750+250+30")
root.resizable(width=FALSE,height=FALSE)

f1 = Frame(root)
# f1.pack()
# f1.place(width=1400, height=750)
f1.config(background="pink")
# img = ImageTk.PhotoImage(Image.open("./img/bg.jpg"))
# panel = Label(f1, image=img)
# panel.pack()


chuoi11 = Text(f1, width=100, height = 10 , font=("Arial",15))
chuoi21 = Text(f1, width=100, height = 10 , font=("Arial",15))
chuoi31 = Text(f1, width=100, height = 10 , font=("Arial",15))
chuoi41 = Text(f1, width=100, height = 10 , font=("Arial",15))
chuoi51 = Text(f1, width=100, height = 10 , font=("Arial",15))

# label tên ứng dụng
Label(f1, text='HỆ THỐNG KIỂM TRA ĐẠO VĂN ( PYTHON )',bg="pink",font=("Arial",28,'bold')).pack(pady=10)
Label(f1,text="Nhập văn bản cần kiểm tra:",font=("Arial",12,"bold"),bg="pink").place(x=70,y=80)
btn_openfile1 = Button(f1,text="Mở dữ liệu trên máy",font=("Arial",12),bg="blue",fg="white",command=open_file1)
btn_openfile1.place(x=300,y=75)
def trove():
    f1.place_forget()
    f2.place(x=0,y=0,width=1400,height=750)

Button(f1,text="Trở về",font=("Arial",12),fg='white',bg="red",command=trove).place(x=20,y=20,width=100)

variable1 = StringVar(f1)
variable1.set("Pink")# default value
w1 = OptionMenu(f1, variable1,"Pink", "MySQL", "Dữ liệu trên máy tính")
w1.config(width=15,font=("Arial",12),bg='orange',fg='white')
w1.place(x=500,y=360)
Label(f1,text="Chọn hình thức tìm kiếm:",font=("Arial",12,'bold'),bg='pink').place(y=365,x=270)
# ô văn bản đầu vào
#Label(f1,text="Văn bản cần kiểm tra:").place(x=10,y=30)
box1 = Text(f1, width=115, height=10, font=("Arial",15),fg="black")
box1.pack(pady=40)
# nút mở file
variable = StringVar(f1)
variable.set("Internet")# default value
w = OptionMenu(f1, variable,"Internet", "MySQL", "Dữ liệu trên máy tính")
w.config(width=19,font=("Arial",12),bg='orange',fg='white')
w.place(x=500,y=360)

# nút tìm kiếm văn bản
btn_timkiem1 = Button(f1,text="Tìm kiếm ( Kiểm tra ) ",font=("Arial",12),bg="green",fg="white",command=timkiem1)
btn_timkiem1.place(x=750,y=360)
# nút xóa văn bản
Button(f1,text="Xóa",font=("Arial",12),bg="red",fg="white",width=5,command=xoa1).place(x=960,y=360)

btn11 = Text(f1, width=135, height=2, font=("Arial", 10))
btn11.place(x=60,y=410)
txt11 = Text(f1, width=10, height=1, font=("Arial", 14))
txt11.place(x=1130,y=410)
show11 = Button(f1,text="Show",font=("Arial",10),bg="blue",fg="white",command=hienthiketqua11)
show11.place(x=1050,y=410)
search11 = Button(f1,text="Search",font=("Arial",10),bg="green",fg="white",command=tracuu11)
search11.place(x=1280,y=410)

btn21 = Text(f1, width=135, height=2, font=("Arial", 10))
btn21.place(x=60,y=465)
txt21 = Text(f1, width=10, height=1, font=("Arial", 14))
txt21.place(x=1130,y=465)
show21 = Button(f1,text="Show",font=("Arial",10),bg="blue",fg="white",command=hienthiketqua21)
show21.place(x=1050,y=465)
search21 = Button(f1,text="Search",font=("Arial",10),bg="green",fg="white",command=tracuu21)
search21.place(x=1280,y=465)

btn31 = Text(f1, width=135, height=2, font=("Arial", 10))
btn31.place(x=60,y=520)
txt31 = Text(f1, width=10, height=1, font=("Arial", 14))
txt31.place(x=1130,y=520)
show31 = Button(f1,text="Show",font=("Arial",10),bg="blue",fg="white",command=hienthiketqua31)
show31.place(x=1050,y=520)
search31 = Button(f1,text="Search",font=("Arial",10),bg="green",fg="white",command=tracuu31)
search31.place(x=1280,y=520)

btn41 = Text(f1, width=135, height=2, font=("Arial", 10))
btn41.place(x=60,y=575)
txt41 = Text(f1, width=10, height=1, font=("Arial", 14))
txt41.place(x=1130,y=575)
show41 = Button(f1,text="Show",font=("Arial",10),bg="blue",fg="white",command=hienthiketqua41)
show41.place(x=1050,y=575)
search41 = Button(f1,text="Search",font=("Arial",10),bg="green",fg="white",command=tracuu41)
search41.place(x=1280,y=575)

btn51 = Text(f1, width=135, height=2, font=("Arial", 10))
btn51.place(x=60,y=630)
txt51 = Text(f1, width=10, height=1, font=("Arial", 14))
txt51.place(x=1130,y=630)
show51 = Button(f1,text="Show",font=("Arial",10),bg="blue",fg="white",command=hienthiketqua51)
show51.place(x=1050,y=630)
search51 = Button(f1,text="Search",font=("Arial",10),bg="green",fg="white",command=tracuu51)
search51.place(x=1280,y=630)

def save_file_excel():
    def kiemtra():
        output_excel_path = './' + str(dulieu.get(1.0, END)).lstrip().rstrip() + '.xlsx'
        if (os.path.exists(output_excel_path) == True):
            # print("ĐÃ tồn tại")
            mbox.showwarning("Thông báo", "Tên file đã tồn tại")
            nhaplieu.destroy()
        else:
            so_dong = len(input_excel)
            for i in myresult:
                input_excel.insert(so_dong+1,[i[0],i[1],i[2],i[3],str(kiemtradaovan1(i[2]))])
            a = sorted(input_excel, key=lambda a_entry: a_entry[4], reverse=True)
            output_Excel(a, output_excel_path)
            mbox.showinfo("Thông báo",
                          "Lưu file thành công\n\nĐường dẫn tới file vừa lưu\n\nC:/Users/nhand/OneDrive/Máy tính/Python/CheckPlagiarism/" + str(
                              dulieu.get(1.0, END)).lstrip().rstrip() + '.xlsx')
            nhaplieu.destroy()

    nhaplieu = Tk()
    nhaplieu.geometry("500x280+800+200")
    nhaplieu.title("Lưu file excel")
    Label(nhaplieu, text="NHẬP TÊN FILE CẦN LƯU", font=("Arial", 17, 'bold')).pack(pady=20)
    dulieu = Text(nhaplieu, width=30, height=2, font=("Arial", 17))
    dulieu.pack(pady=10)
    Button(nhaplieu, text="Save file", font=("Arial", 17), bg="light green",command=kiemtra).pack(pady=30)
    nhaplieu.mainloop()

save_ex = Button(f1,text="SAVE FILE EXCEL",font=("Arial",10),bg='light blue',command=save_file_excel)
save_ex.place(x=600,y=690)
save_ex.place_forget()

kiemtrathienthi1()

btn11.config(state=DISABLED)
btn21.config(state=DISABLED)
btn31.config(state=DISABLED)
btn41.config(state=DISABLED)
btn51.config(state=DISABLED)

txt11.config(state=DISABLED)
txt21.config(state=DISABLED)
txt31.config(state=DISABLED)
txt41.config(state=DISABLED)
txt51.config(state=DISABLED)

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
def show_f1():
    f2.place_forget()
    f1.pack()
    f1.place(width=1400, height=750)

nhan = ImageTk.PhotoImage(Image.open("./img/nhan.jpg"))
kiet = ImageTk.PhotoImage(Image.open("./img/kiet.jpg"))
trung = ImageTk.PhotoImage(Image.open("./img/trung.jpg"))
logo = ImageTk.PhotoImage(Image.open("./img/proxy_form.png"))
def show_info():
    f3 = Frame(root)
    f3.pack()
    f3.place(width=1400, height=750)
    f3.config(background="pink")
    def get_fanpage1():
        webbrowser.open("https://www.facebook.com/do.nhan.16940599/")
    def get_fanpage2():
        webbrowser.open("https://www.facebook.com/tkiiet2507")
    def get_fanpage3():
        webbrowser.open("https://www.facebook.com/profile.php?id=100009729399322")
    Label(f3,image=nhan,bd=0).place(x=130,y=100)
    Button(f3,text="Đỗ Trọng Nhân",font=("Arial",12,'bold'),bg='light yellow',command=get_fanpage1).place(x=210,y=420)
    Label(f3, image=kiet, bd=0).place(x=530, y=100)
    Button(f3, text="Trần Tuấn Kiệt", font=("Arial", 12, 'bold'), bg='light green',command=get_fanpage2).place(x=610, y=420)
    Label(f3, image=trung, bd=0).place(x=930, y=100)
    Button(f3, text="Nguyễn Quang Trung", font=("Arial", 12, 'bold'), bg='light blue',command=get_fanpage3).place(x=1010, y=420)
    Label(f3, text="Ngày phát hành: 11/2021", font=("Arial", 16, 'bold'), fg="black", bg='pink').place(x=130,y=500)
    Label(f3, text="Ngôn ngữ sử dụng: PYTHON", font=("Arial", 16, 'bold'), fg="black", bg='pink').place(x=130, y=540)
    Label(f3, text="Đơn vị phát triển và cung cấp ứng dụng: DAUCATMOI Team", font=("Arial", 16, 'bold'), fg="black", bg='pink').place(x=130, y=580)
    Label(f3, text="Thông tin liên hệ: dotrongnhan15102000@gmail.com", font=("Arial", 16, 'bold'), fg="black", bg='pink').place(x=130, y=620)
    Label(f3,image=logo,bd=0).place(y=500,x=1000)
    def quayve():
        f3.place_forget()
        f2.place(width=1400, height=750)
    Button(f3,text="Trở về",bg='red',fg='white',command=quayve).place(x=10,y=10,width=80)
    Label(f3, text='THÔNG TIN ỨNG DỤNG', bg="pink", font=("Arial", 28, 'bold')).pack(pady=10)

def exit_app():
    rs = mbox.askyesno("Xác nhận thoát ứng dụng","Bạn có muốn thoát ứng dụng")
    if rs == 1:
        root.quit()

f2 = Frame(root)
f2.pack()
f2.place(width=1400, height=750)
f2.config(background="white")
Label(f2,text='CHÀO MỪNG BẠN ĐẾN VỚI HỆ THỐNG KIỂM TRA ĐẠO VĂN',font=("Arial",16,'bold'),bg='white').place(x=400,y=670)
hide_f1 = Button(f2,text="ĐĂNG NHẬP VÀO ỨNG DỤNG",bg="light yellow",font=("Arial",10,'bold'),command=show_f1)
hide_f1.place(x=500,y=715)
exit_f1 = Button(f2,text="THOÁT ỨNG DỤNG",bg="RED",font=("Arial",10,'bold'),command=exit_app)
exit_f1.place(x=800,y=715)

hinh11 = ImageTk.PhotoImage(Image.open("./img/images.png"))
hinh21 = ImageTk.PhotoImage(Image.open("./img/hutech1.jpg"))
hinh31 = ImageTk.PhotoImage(Image.open("./img/hutech2.jpg"))
hinh41 = ImageTk.PhotoImage(Image.open("./img/hutech3.png"))
hinh5 = ImageTk.PhotoImage(Image.open("./img/info.jpg"))
hinh1 = ImageTk.PhotoImage(Image.open("./img/free-plagiarism-checker-for-teachers-updated-1.jpg"))
hinh2 = ImageTk.PhotoImage(Image.open("./img/2020_11_09______5a65c818ae7ed57f2a2e197a16802592.jpg"))
hinh3 = ImageTk.PhotoImage(Image.open("./img/Untitled-6-800x450.jpg"))
hinh4 = ImageTk.PhotoImage(Image.open("./img/chong-dao-van.jpg"))

label5 = Button(f2,image= hinh5,bd=0,command=show_info)
label5.place(x=1300,y=660)

label11 = Label(f2,image= hinh11,bd=0,bg='white')
label11.pack()
label11.place(x=0,y=0,width=647,height=650)

label1 = Label(f2,image= hinh1,bd=0,bg='white')
label1.pack()
label1.place(x=650,y=0,height=600,width=750)
x=1
x1=1
def move():
    global x
    if x>4:
        x=1
    if x==1:
        label1.config(image=hinh1)
    elif x==2:
        label1.config(image=hinh2)
    elif x==3:
        label1.config(image=hinh3)
    elif x==4:
        label1.config(image=hinh4)
    x+=1
    label1.after(2000,move)

def move1():
    global x1
    if x1>4:
        x1=1
    if x1==1:
        label11.config(image=hinh11)
    elif x1==2:
        label11.config(image=hinh21)
    elif x1==3:
        label11.config(image=hinh31)
    elif x1==4:
        label11.config(image=hinh41)
    x1+=1
    label11.after(2000,move1)

move()
move1()

root.mainloop()


