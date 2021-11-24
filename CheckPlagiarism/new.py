from tkinter import *
from tkinter import filedialog
import webbrowser
from googlesearch import search
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
import tkinter.messagebox as mbox


window = Tk()
window.title("Ứng dụng kiểm tra đạo văn")
window.resizable(width=FALSE,height=FALSE)
window.geometry("800x400+600+100")

def tiengviet():
    app = Tk()
    app.title("Kiểm tra đạo văn ( Tiếng Việt )")
    app.resizable(width=FALSE,height=FALSE)
    app.geometry("1200x750+300+100")

    # từ dừng trong tiếng việt (dùng để xử lý ngôn ngữ tự nhiên)
    tudung = ['a lô', 'a ha', 'ai', 'ai ai', 'ai nấy', 'ai đó', 'alô', 'amen', 'anh', 'anh ấy', 'ba', 'ba ba', 'ba bản',
              'ba cùng', 'ba họ', 'ba ngày', 'ba ngôi', 'ba tăng', 'bao giờ', 'bao lâu', 'bao nhiêu', 'bao nả',
              'bay biến', 'biết', 'biết bao', 'biết bao nhiêu', 'biết chắc',
              'biết chừng nào', 'biết mình', 'biết mấy', 'biết thế', 'biết trước', 'biết việc', 'biết đâu',
              'biết đâu chừng',
              'biết đâu đấy', 'biết được', 'buổi', 'buổi làm', 'buổi mới', 'buổi ngày', 'buổi sớm', 'bà', 'bà ấy',
              'bài', 'bài bác', 'bài bỏ', 'bài cái', 'bác',
              'bán', 'bán cấp', 'bán dạ', 'bán thế', 'bây bẩy', 'bây chừ', 'bây giờ', 'bây nhiêu', 'bèn', 'béng', 'bên',
              'bên bị', 'bên có', 'bên cạnh', 'bông', 'bước', 'bước khỏi', 'bước tới', 'bước đi', 'bạn', 'bản',
              'bản bộ', 'bản riêng', 'bản thân', 'bản ý', 'bất chợt', 'bất cứ', 'bất giác', 'bất kì', 'bất kể',
              'bất kỳ', 'bất luận', 'bất ngờ', 'bất nhược', 'bất quá', 'bất quá chỉ', 'bất thình lình', 'bất tử',
              'bất đồ',
              'bấy', 'bấy chầy', 'bấy chừ', 'bấy giờ', 'bấy lâu', 'bấy lâu nay', 'bấy nay', 'bấy nhiêu',
              'bập bà bập bõm', 'bập bõm', 'bắt đầu', 'bắt đầu từ', 'bằng', 'bằng cứ', 'bằng không', 'bằng người',
              'bằng nhau', 'bằng như',
              'bằng nào', 'bằng nấy', 'bằng vào', 'bằng được', 'bằng ấy', 'bển', 'bệt', 'bị', 'bị chú', 'bị vì', 'bỏ',
              'bỏ bà', 'bỏ cha', 'bỏ cuộc', 'bỏ không', 'bỏ lại',
              'bỏ mình', 'bỏ mất', 'bỏ mẹ', 'bỏ nhỏ', 'bỏ quá', 'bỏ ra', 'bỏ riêng', 'bỏ việc', 'bỏ xa', 'bỗng',
              'bỗng chốc', 'bỗng dưng', 'bỗng không',
              'bỗng nhiên', 'bỗng nhưng', 'bỗng thấy', 'bỗng đâu', 'bộ', 'bộ thuộc', 'bộ điều', 'bội phần', 'bớ', 'bởi',
              'bởi ai', 'bởi chưng', 'bởi nhưng', 'bởi sao', 'bởi thế', 'bởi thế cho nên', 'bởi tại', 'bởi vì',
              'bởi vậy',
              'bởi đâu', 'bức', 'cao', 'cao lâu', 'cao ráo', 'cao răng', 'cao sang', 'cao số', 'cao thấp', 'cao thế',
              'cao xa', 'cha', 'cha chả', 'chao ôi', 'chia sẻ', 'chiếc', 'cho', 'cho biết', 'cho chắc', 'cho hay',
              'cho nhau', 'cho nên', 'cho rằng', 'cho rồi', 'cho thấy',
              'cho tin', 'cho tới', 'cho tới khi', 'cho về', 'cho ăn', 'cho đang', 'cho được', 'cho đến', 'cho đến khi',
              'cho đến nỗi', 'choa', 'chu cha', 'chui cha', 'chung', 'chung cho',
              'chung chung', 'chung cuộc', 'chung cục', 'chung nhau', 'chung qui', 'chung quy', 'chung quy lại',
              'chung ái', 'chuyển', 'chuyển tự', 'chuyển đạt', 'chuyện', 'chuẩn bị', 'chành chạnh', 'chí chết', 'chính',
              'chính bản', 'chính giữa', 'chính là', 'chính thị', 'chính điểm', 'chùn chùn', 'chùn chũn', 'chú',
              'chú dẫn', 'chú khách', 'chú mày', 'chú mình', 'chúng', 'chúng mình', 'chúng ta', 'chúng tôi',
              'chúng ông', 'chăn chắn', 'chăng', 'chăng chắc', 'chăng nữa', 'chơi', 'chơi họ', 'chưa',
              'chưa bao giờ', 'chưa chắc', 'chưa có', 'chưa cần', 'chưa dùng', 'chưa dễ',
              'chưa kể', 'chưa tính',
              'chưa từng', 'chầm chập',
              'chậc', 'chắc', 'chắc chắn',
              'chắc dạ', 'chắc hẳn', 'chắc lòng',
              'chắc người', 'chắc vào', 'chắc ăn',
              'chẳng lẽ', 'chẳng những', 'chẳng nữa',
              'chẳng phải', 'chết nỗi', 'chết thật',
              'chết tiệt', 'chỉ', 'chỉ chính',
              'chỉ có', 'chỉ là', 'chỉ tên',
              'chỉn', 'chị', 'chị bộ', 'chị ấy',
              'chịu', 'chịu chưa', 'chịu lời', 'chịu tốt',
              'chịu ăn', 'chọn', 'chọn bên', 'chọn ra',
              'chốc chốc', 'chớ', 'chớ chi', 'chớ gì',
              'chớ không', 'chớ kể', 'chớ như', 'chợt', 'chợt nghe',
              'chợt nhìn', 'chủn', 'chứ', 'chứ ai', 'chứ còn', 'chứ gì',
              'chứ không', 'chứ không phải', 'chứ lại', 'chứ lị',
              'chứ như', 'chứ sao', 'coi bộ', 'coi mòi', 'con',
              'con con', 'con dạ', 'con nhà', 'con tính', 'cu cậu', 'cuối', 'cuối cùng', 'cuối điểm', 'cuốn', 'cuộc',
              'càng', 'càng càng', 'càng hay', 'cá nhân', 'các', 'các cậu', 'cách', 'cách bức', 'cách không',
              'cách nhau',
              'cách đều', 'cái',
              'cái gì', 'cái họ', 'cái đã',
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
              'tốt hơn', 'tốt mối', 'tốt ngày', 'tột', 'tột cùng', 'tớ', 'tới', 'tới gần', 'tới mức', 'tới nơi',
              'tới thì', 'tức thì', 'tức tốc', 'từ', 'từ căn', 'từ giờ', 'từ khi', 'từ loại', 'từ nay', 'từ thế',
              'từ tính',
              'từ tại', 'từ từ', 'từ ái', 'từ điều', 'từ đó', 'từ ấy', 'từng', 'từng cái', 'từng giờ', 'từng nhà',
              'từng phần',
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
              'đưa tới', 'đưa vào', 'đưa về', 'đưa xuống', 'đưa đến', 'được', 'được cái', 'được lời', 'được nước',
              'được tin', 'đại loại',
              'đại nhân', 'đại phàm', 'đại để', 'đạt', 'đảm bảo', 'đầu tiên', 'đầy', 'đầy năm',
              'đầy phè', 'đầy tuổi', 'đặc biệt', 'đặt', 'đặt làm', 'đặt mình', 'đặt mức', 'đặt ra', 'đặt trước',
              'đặt để', 'đến', 'đến bao giờ', 'đến cùng', 'đến cùng cực', 'đến cả', 'đến giờ', 'đến gần', 'đến hay',
              'đến khi', 'đến lúc', 'đến lời',
              'đến nay', 'đến ngày', 'đến nơi', 'đến nỗi', 'đến thì', 'đến thế', 'đến tuổi', 'đến xem', 'đến điều',
              'đến đâu', 'đều', 'đều bước', 'đều nhau', 'đều đều', 'để', 'để cho', 'để giống', 'để không', 'để lòng',
              'để lại', 'để mà', 'để phần', 'để được', 'để đến nỗi', 'đối với', 'đồng thời', 'đủ', 'đủ dùng', 'đủ nơi',
              'đủ số', 'đủ điều', 'đủ điểm', 'ơ',
              'ơ hay', 'ơ kìa', 'ơi', 'ơi là', 'ư', 'ạ', 'ạ ơi', 'ấy', 'ấy là', 'ầu ơ', 'ắt', 'ắt hẳn', 'ắt là',
              'ắt phải', 'ắt thật', 'ối dào', 'ối giời', 'ối giời ơi', 'ồ', 'ồ ồ', 'ổng', 'ớ', 'ớ này', 'ờ', 'ờ ờ', 'ở',
              'ở lại', 'ở như', 'ở nhờ', 'ở năm', 'ở trên', 'ở vào', 'ở đây', 'ở đó', 'ở được', 'ủa', 'ứ hự', 'ứ ừ',
              'ừ', 'ừ nhé', 'ừ thì', 'ừ ào', 'ừ ừ', 'ử', ]

    # hàm xóa sạch các textbox
    def clear():
        box1.delete(1.0, END)
        box1.focus()
        btn1.delete(1.0, END)
        btn2.delete(1.0, END)
        btn3.delete(1.0, END)
        btn4.delete(1.0, END)
        btn5.delete(1.0, END)
        txt1.delete(1.0, END)
        txt2.delete(1.0, END)
        txt3.delete(1.0, END)
        txt4.delete(1.0, END)
        txt5.delete(1.0, END)

    chuoi1 = Text(app, width=100, height=10, font=("Arial", 15))
    chuoi2 = Text(app, width=100, height=10, font=("Arial", 15))
    chuoi3 = Text(app, width=100, height=10, font=("Arial", 15))
    chuoi4 = Text(app, width=100, height=10, font=("Arial", 15))
    chuoi5 = Text(app, width=100, height=10, font=("Arial", 15))

    # hàm search của google
    def timkiem():
        if len(box1.get(1.0, END)) <= 10:
            mbox.showwarning("Thông báo!", "Không được để trống hoặc ít hơn 50 ký tự!")
        else:
            # set trạng thái edit
            btn1.config(state=NORMAL)
            btn2.config(state=NORMAL)
            btn3.config(state=NORMAL)
            btn4.config(state=NORMAL)
            btn5.config(state=NORMAL)

            txt1.config(state=NORMAL)
            txt2.config(state=NORMAL)
            txt3.config(state=NORMAL)
            txt4.config(state=NORMAL)
            txt5.config(state=NORMAL)

            btn1.delete(1.0, END)
            btn2.delete(1.0, END)
            btn3.delete(1.0, END)
            btn4.delete(1.0, END)
            btn5.delete(1.0, END)
            txt1.delete(1.0, END)
            txt2.delete(1.0, END)
            txt3.delete(1.0, END)
            txt4.delete(1.0, END)
            txt5.delete(1.0, END)
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
                    btn1.insert(END, i)
                    txt1.insert(END, tile)
                    if tile == 0:
                        chuoi1.insert(END, "")
                    else:
                        chuoi1.insert(END, result)
                if dem == 2:
                    btn2.insert(END, i)
                    txt2.insert(END, tile)
                    if tile == 0:
                        chuoi2.insert(END, "")
                    else:
                        chuoi2.insert(END, result)
                if dem == 3:
                    btn3.insert(END, i)
                    txt3.insert(END, tile)
                    if tile == 0:
                        chuoi3.insert(END, "")
                    else:
                        chuoi3.insert(END, result)
                if dem == 4:
                    btn4.insert(END, i)
                    txt4.insert(END, tile)
                    if tile == 0:
                        chuoi4.insert(END, "")
                    else:
                        chuoi4.insert(END, result)
                if dem == 5:
                    btn5.insert(END, i)
                    txt5.insert(END, tile)
                    if tile == 0:
                        chuoi5.insert(END, "")
                    else:
                        chuoi5.insert(END, result)
                    # set trạng thái readonly
                    btn1.config(state=DISABLED)
                    btn2.config(state=DISABLED)
                    btn3.config(state=DISABLED)
                    btn4.config(state=DISABLED)
                    btn5.config(state=DISABLED)

                    txt1.config(state=DISABLED)
                    txt2.config(state=DISABLED)
                    txt3.config(state=DISABLED)
                    txt4.config(state=DISABLED)
                    txt5.config(state=DISABLED)

                    mbox.showinfo("Thông báo", "Kết thúc tìm kiếm")
                    kiemtrathienthi()

    # hàm hiển thị kết quả tìm được ra textbox
    def hienthiketqua1():
        if len(chuoi1.get(1.0, END)) < 1:
            mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
        else:
            app1 = Tk()
            app1.title("Đoạn văn trùng khớp")
            dv = Text(app1, width=100, height=10, font=("Arial", 15), )
            dv.pack(pady=0)
            dv.insert(END, chuoi1.get(1.0, END))
            app1.mainloop()

    def hienthiketqua2():
        if len(chuoi2.get(1.0, END)) <= 1:
            mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
        else:
            app2 = Tk()
            app2.title("Đoạn văn trùng khớp")
            dv = Text(app2, width=100, height=10, font=("Arial", 15))
            dv.pack(pady=0)
            dv.insert(END, chuoi2.get(1.0, END))
            app2.mainloop()

    def hienthiketqua3():
        if len(chuoi3.get(1.0, END)) < 1:
            mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
        else:
            app3 = Tk()
            app3.title("Đoạn văn trùng khớp")
            dv = Text(app3, width=100, height=10, font=("Arial", 15), )
            dv.pack(pady=0)
            dv.insert(END, chuoi3.get(1.0, END))
            app3.mainloop()

    def hienthiketqua4():
        if len(chuoi4.get(1.0, END)) < 1:
            mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
        else:
            app4 = Tk()
            app4.title("Đoạn văn trùng khớp")
            dv = Text(app4, width=100, height=10, font=("Arial", 15), )
            dv.pack(pady=0)
            dv.insert(END, chuoi4.get(1.0, END))
            app4.mainloop()

    def hienthiketqua5():
        if len(chuoi5.get(1.0, END)) < 1:
            mbox.showerror("Thông báo", "Không tìm thấy đoạn văn trùng khớp")
        else:
            app5 = Tk()
            app5.title("Đoạn văn trùng khớp")
            dv = Text(app5, width=100, height=10, font=("Arial", 15), )
            dv.pack(pady=0)
            dv.insert(END, chuoi5.get(1.0, END))
            app5.mainloop()

    # hàm mở file
    def open_file():
        text_file = filedialog.askopenfilename(initialdir="This PC:/", title="Open Text",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'r', encoding='UTF-8')
        stuff = text_file.read()
        box1.insert(END, str(stuff).lstrip().rstrip())
        text_file.close()

    # hàm kiểm tra trùng lặp văn bản
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
        rs = round(cosine, 2)
        result = str(rs) + "%"
        return result

    # ký tự tiếng việt cần chuyển sang không dấu
    patterns = {
        '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
        '[đ]': 'd',
        '[èéẻẽẹêềếểễệ]': 'e',
        '[ìíỉĩị]': 'i',
        '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
        '[ùúủũụưừứửữự]': 'u',
        '[ỳýỷỹỵ]': 'y'
    }

    # hàm chuyển đổi có dấu thành không dấu
    def convert(text):
        output = text
        for regex, replace in patterns.items():
            output = re.sub(regex, replace, output)
            # deal with upper case
            output = re.sub(regex.upper(), replace.upper(), output)
        return output

    Label(app, text="Kiểm tra xác suất trùng lặp văn bản", font=("Arial", 20)).pack(pady=10)

    box1 = Text(app, width=100, height=10, font=("Arial", 15))
    box1.pack(pady=10)

    btn_openfile = Button(app, text="Open File", font=("Arial", 12), bg="green", fg="white", command=open_file)
    btn_openfile.place(x=350, y=330)

    btn_timkiem = Button(app, text="Text Search", font=("Arial", 12), bg="green", fg="white", command=timkiem)
    btn_timkiem.place(x=550, y=330)

    Button(app, text="Delete", font=("Arial", 12), bg="red", fg="white", width=5, command=clear).place(x=700, y=330)

    # hàm tra cứu kết quả tìm được
    def tracuu1():
        webbrowser.open(btn1.get(1.0, END))

    def tracuu2():
        webbrowser.open(btn2.get(1.0, END))

    def tracuu3():
        webbrowser.open(btn3.get(1.0, END))

    def tracuu4():
        webbrowser.open(btn4.get(1.0, END))

    def tracuu5():
        webbrowser.open(btn5.get(1.0, END))

    # hàm tắt/bật các button
    def kiemtrathienthi():
        if (len(btn1.get(1.0, END)) <= 1):
            show1.config(state=DISABLED)
            search1.config(state=DISABLED)
        else:
            show1.config(state=NORMAL)
            search1.config(state=NORMAL)

        if (len(btn2.get(1.0, END)) <= 1):
            show2.config(state=DISABLED)
            search2.config(state=DISABLED)
        else:
            show2.config(state=NORMAL)
            search2.config(state=NORMAL)

        if (len(btn3.get(1.0, END)) <= 1):
            show3.config(state=DISABLED)
            search3.config(state=DISABLED)
        else:
            show3.config(state=NORMAL)
            search3.config(state=NORMAL)

        if (len(btn4.get(1.0, END)) <= 1):
            show4.config(state=DISABLED)
            search4.config(state=DISABLED)
        else:
            show4.config(state=NORMAL)
            search4.config(state=NORMAL)

        if (len(btn5.get(1.0, END)) <= 1):
            show5.config(state=DISABLED)
            search5.config(state=DISABLED)
        else:
            show5.config(state=NORMAL)
            search5.config(state=NORMAL)

    btn1 = Text(app, width=120, height=2, font=("Arial", 10))
    btn1.place(x=50, y=380)
    txt1 = Text(app, width=10, height=1, font=("Arial", 14))
    txt1.place(x=970, y=380)
    show1 = Button(app, text="Show", font=("Arial", 10), bg="blue", fg="white", command=hienthiketqua1)
    show1.place(x=910, y=380)
    search1 = Button(app, text="Search", font=("Arial", 10), bg="green", fg="white", command=tracuu1)
    search1.place(x=1100, y=380)

    btn2 = Text(app, width=120, height=2, font=("Arial", 10))
    btn2.place(x=50, y=450)
    txt2 = Text(app, width=10, height=1, font=("Arial", 14))
    txt2.place(x=970, y=450)
    show2 = Button(app, text="Show", font=("Arial", 10), bg="blue", fg="white", command=hienthiketqua2)
    show2.place(x=910, y=450)
    search2 = Button(app, text="Search", font=("Arial", 10), bg="green", fg="white", command=tracuu2)
    search2.place(x=1100, y=450)

    btn3 = Text(app, width=120, height=2, font=("Arial", 10))
    btn3.place(x=50, y=520)
    txt3 = Text(app, width=10, height=1, font=("Arial", 14))
    txt3.place(x=970, y=520)
    show3 = Button(app, text="Show", font=("Arial", 10), bg="blue", fg="white", command=hienthiketqua3)
    show3.place(x=910, y=520)
    search3 = Button(app, text="Search", font=("Arial", 10), bg="green", fg="white", command=tracuu3)
    search3.place(x=1100, y=520)

    btn4 = Text(app, width=120, height=2, font=("Arial", 10))
    btn4.place(x=50, y=590)
    txt4 = Text(app, width=10, height=1, font=("Arial", 14))
    txt4.place(x=970, y=590)
    show4 = Button(app, text="Show", font=("Arial", 10), bg="blue", fg="white", command=hienthiketqua4)
    show4.place(x=910, y=590)
    search4 = Button(app, text="Search", font=("Arial", 10), bg="green", fg="white", command=tracuu4)
    search4.place(x=1100, y=590)

    btn5 = Text(app, width=120, height=2, font=("Arial", 10))
    btn5.place(x=50, y=660)
    txt5 = Text(app, width=10, height=1, font=("Arial", 14))
    txt5.place(x=970, y=660)
    show5 = Button(app, text="Show", font=("Arial", 10), bg="blue", fg="white", command=hienthiketqua5)
    show5.place(x=910, y=660)
    search5 = Button(app, text="Search", font=("Arial", 10), bg="green", fg="white", command=tracuu5)
    search5.place(x=1100, y=660)

    kiemtrathienthi()

    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)

    txt1.config(state=DISABLED)
    txt2.config(state=DISABLED)
    txt3.config(state=DISABLED)
    txt4.config(state=DISABLED)
    txt5.config(state=DISABLED)

    app.mainloop()

def tienganh():
    window2 = Tk()
    window2.title("Kiểm tra đạo văn ( Tiếng Anh )")
    window2.resizable(width=FALSE,height=FALSE)
    window2.geometry("1200x750+300+100")
    window2.mainloop()

def closewindow():
    window.destroy()


Label(window,text="KIỂM TRA ĐẠO VĂN",font=("Arial",30),fg="red").pack(pady=40)
Button(window,text="Kiểm Tra Văn Bản Tiếng Việt",font=("Arial",20),bg="pink",command=tiengviet).pack(pady=10)
Button(window,text="Kiểm Tra Văn Bản Tiếng Anh",font=("Arial",20),bg="orange",command=tienganh).pack(pady=20)
Button(window,text="Exit",font=("Arial",15),bg="red",command=closewindow).pack(pady=20)
window.mainloop()