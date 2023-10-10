from newsplease import NewsPlease


# text  = """Hiệp hội các quốc gia Đông Nam Á (ASEAN) sẽ không từ bỏ nỗ lực chấm dứt bạo lực ở đất nước thành viên Myanmar, mặc dù quân đội cầm quyền tại đây không có tiến triển nào trong kế hoạch hòa bình mà họ đã nhất trí với khối hai năm trước, Indonesia cho biết hôm thứ Năm (11/5).\nSự thất vọng đã gia tăng trong một số thành viên của khối gồm 10 quốc gia đối với Myanmar, và cách xử lý tình trạng hỗn loạn chính trị đẫm máu của nước này đã đặt ra câu hỏi về tính hiệu quả và sự thống nhất của khối.\nTổng thống Indonesia Joko Widodo thẳng thắn chỉ trích và nói tại một hội nghị thượng đỉnh ASEAN ở thị trấn Labuan Bajo của Indonesia rằng các tướng lĩnh của Myanmar đã không có một tiến bộ nào trong kế hoạch hòa bình ASEAN gồm 5 điểm.\nÔng cũng nói rằng những vi phạm nhân quyền ở Myanmar là không thể dung thứ và bạo lực ở đó cần phải được chấm dứt và người dân của họ phải được bảo vệ.\nIndonesia là chủ tịch ASEAN năm nay. Ngoại trưởng nước này, bà Retno Marsudi, phát biểu tại hội nghị thượng đỉnh rằng các nguyên tắc dân chủ và pháp quyền đã được ghi trong hiến chương ASEAN.\n“Thiếu tiến bộ không có nghĩa là chúng ta nên từ bỏ”, bà Retno nói khi bế mạc hội nghị thượng đỉnh.\nMyanmar đã rơi vào tình trạng hỗn loạn dữ dội kể từ khi quân đội lật đổ chính phủ do khôi nguyên Nobel Hòa bình Aung San Suu Kyi lãnh đạo vào năm 2021.\nCuộc đảo chính đã gây ra các cuộc biểu tình lan rộng khiến quân đội đàn áp dữ dội. Kể từ đó, quân đội đã chiến đấu với quân nổi dậy dân tộc thiểu số tìm kiếm quyền tự quyết và các chiến binh đồng minh ủng hộ dân chủ.\nTháng trước, ASEAN lên án quân đội Myanmar về một trong những cuộc không kích mới nhất và nguy hiểm nhất khiến ít nhất 100 người thiệt mạng. Chính quyền nói rằng họ đang chiến đấu với “những kẻ khủng bố”.\nVới tư cách là chủ tịch ASEAN, Indonesia đã nói chuyện với tất cả các bên trong những tháng gần đây nhằm nỗ lực giúp các cuộc đàm phán diễn ra, nhưng sự chỉ trích từ Indonesia hôm thứ Năm cho thấy nỗ lực này không mang lại bất kỳ kết quả nào.\n“Tôi phải nói thẳng. Về việc thực hiện 5 điểm là không có tiến triển đáng kể”, ông Jokowi nói trước đó, đề cập đến cái mà ASEAN gọi là “đồng thuận 5 điểm” hay “5PC” cho Myanmar.\nVị tướng lãnh đạo hàng đầu của Myanmar đã đồng ý với kế hoạch kêu gọi chấm dứt bạo lực, tiếp cận nhân đạo và đối thoại giữa tất cả các bên, vào tháng 4 năm 2021 tại một cuộc họp ở Jakarta, nhưng quân đội phần lớn đã phớt lờ kế hoạch này.\nASEAN, trong nhiều năm tuân thủ nguyên tắc không can thiệp vào công việc nội bộ của nhau, đã cấm các nhà lãnh đạo chính quyền Myanmar tham dự các cuộc họp cấp cao của khối này vì không thực hiện kế hoạch.\nTổng thư ký ASEAN Kao Kim Hourn nói với Reuters bên lề hội nghị thượng đỉnh rằng kế hoạch vẫn sẽ đóng vai trò là nền tảng trong việc can dự vào chính quyền quân sự.\n“Những gì chúng ta nên làm là đảm bảo rằng bạo lực bị loại bỏ. Đó là điểm mấu chốt”, ông nói.\n“Người ta nói muốn tới đích thì chạy, chạy không được thì đi bộ, không đi được thì bò. Chừng nào còn tiến lên được thì còn có tiến bộ”.\nNgoại trưởng Malaysia, Zambry Abdul Kadir, cho biết khối này rất nghiêm túc về Myanmar “nhưng phải đoàn kết với nhau”.\nÔng nói: “Mọi người đều muốn tìm một giải pháp hòa bình và lâu dài”.\nTrong khi Myanmar chủ trì các cuộc đàm phán trong tuần này, nhóm này cũng thảo luận về những căng thẳng đang gia tăng ở Biển Đông, nơi mà Trung Quốc chủ yếu tuyên bố chủ quyền bất chấp những tuyên bố chồng chéo của một số thành viên ASEAN.\nIndonesia kêu gọi tự kiềm chế trong giải quyết tranh chấp lãnh thổ trên tuyến đường thủy chiến lược."""


def get_content(links: list[str] = None):
    """
    Get the content of the provided article link.

    Args:
        link (str): The link to a article.

    Returns:
        Str : The content of the article
    """
    if links:
        texts = []
        for link in links:
            try:
                article = NewsPlease.from_url(link)
                text = article.maintext
                texts.append
            except Exception as e:
                print(f"Couldn't get the content from link {link}, try again!")
                print(f"Error: {e}")

        return text
    else:
        print("Please give a article links")
