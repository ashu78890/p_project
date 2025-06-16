    # from pptx import Presentation
    # from pptx.util import Pt, Inches, Emu
    # from pptx.dml.color import RGBColor
    # from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE

    # # JSON input
    # json_data = {
    #     "slides": [
    #         {
    #             "shapes": [
    #                 {
    #                     "height": 6858000,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 12189866,
    #                     "x": 0,
    #                     "y": 0
    #                 },
    #                 {
    #                     "height": 565099,
    #                     "text": "bullet point",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 11822278,
    #                     "x": 187452,
    #                     "y": 191110
    #                 },
    #                 {
    #                     "height": 4633265,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 4633265,
    #                     "x": -1979676,
    #                     "y": 1512418
    #                 },
    #                 {
    #                     "height": 4136746,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 4136746,
    #                     "x": 856793,
    #                     "y": 1760220
    #                 },
    #                 {
    #                     "height": 3984955,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 3984955,
    #                     "x": 208483,
    #                     "y": 1836115
    #                 },
    #                 {
    #                     "height": 3794760,
    #                     "image_filename": "slide_1_image.png",
    #                     "type": "PICTURE",
    #                     "width": 3794760,
    #                     "x": 302666,
    #                     "y": 1929384
    #                 },
    #                 {
    #                     "height": 590702,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 590702,
    #                     "x": 3222346,
    #                     "y": 1555394
    #                 },
    #                 {
    #                     "height": 500177,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 3268980,
    #                     "y": 1598371
    #                 },
    #                 {
    #                     "height": 371246,
    #                     "text": "01",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 3268980,
    #                     "y": 1666951
    #                 },
    #                 {
    #                     "height": 309982,
    #                     "text": "Page Speed",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 8164678,
    #                     "x": 3852367,
    #                     "y": 1000354
    #                 },
    #                 {
    #                     "height": 0,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 1105510,
    #                     "x": 3920033,
    #                     "y": 1403604
    #                 },
    #                 {
    #                     "height": 277063,
    #                     "text": "Optimize images and minify CSS for faster loading.",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 8164678,
    #                     "x": 3852367,
    #                     "y": 1497787
    #                 },
    #                 {
    #                     "height": 590702,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 590702,
    #                     "x": 4478731,
    #                     "y": 2609698
    #                 },
    #                 {
    #                     "height": 500177,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 4521708,
    #                     "y": 2657246
    #                 },
    #                 {
    #                     "height": 371246,
    #                     "text": "02",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 4521708,
    #                     "y": 2721254
    #                 },
    #                 {
    #                     "height": 309982,
    #                     "text": "Mobile Friendly",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 6800393,
    #                     "x": 5205679,
    #                     "y": 2505456
    #                 },
    #                 {
    #                     "height": 0,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 1105510,
    #                     "x": 5274259,
    #                     "y": 2905049
    #                 },
    #                 {
    #                     "height": 460858,
    #                     "text": "Use responsive design to improve mobile user experience.",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 6800393,
    #                     "x": 5205679,
    #                     "y": 3001975
    #                 },
    #                 {
    #                     "height": 590702,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 590702,
    #                     "x": 4510735,
    #                     "y": 4370832
    #                 },
    #                 {
    #                     "height": 500177,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 4557370,
    #                     "y": 4417466
    #                 },
    #                 {
    #                     "height": 371246,
    #                     "text": "03",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 4557370,
    #                     "y": 4482389
    #                 },
    #                 {
    #                     "height": 309982,
    #                     "text": "SEO Practices",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 6757416,
    #                     "x": 5248656,
    #                     "y": 4265676
    #                 },
    #                 {
    #                     "height": 0,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 1105510,
    #                     "x": 5317236,
    #                     "y": 4668926
    #                 },
    #                 {
    #                     "height": 460858,
    #                     "text": "Implement proper keywords and meta tags for better rankings.",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 6757416,
    #                     "x": 5248656,
    #                     "y": 4763110
    #                 },
    #                 {
    #                     "height": 590702,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 590702,
    #                     "x": 3222346,
    #                     "y": 5512003
    #                 },
    #                 {
    #                     "height": 500177,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 3268980,
    #                     "y": 5558638
    #                 },
    #                 {
    #                     "height": 371246,
    #                     "text": "04",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 500177,
    #                     "x": 3268980,
    #                     "y": 5623560
    #                 },
    #                 {
    #                     "height": 309982,
    #                     "text": "Content Quality",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 8164678,
    #                     "x": 3852367,
    #                     "y": 5875020
    #                 },
    #                 {
    #                     "height": 0,
    #                     "text": "",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 1105510,
    #                     "x": 3920033,
    #                     "y": 6278270
    #                 },
    #                 {
    #                     "height": 277063,
    #                     "text": "Create relevant and engaging content to boost user retention.",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 8164678,
    #                     "x": 3852367,
    #                     "y": 6375197
    #                 }
    #             ],
    #             "slide_number": 1
    #         },
    #         {
    #             "shapes": [
    #                 {
    #                     "height": 6858000,
    #                     "text": "{\"imagesData\":{\"static1\":{\"id\":\"671f477c3000d7fc3c2e77aa\",\"keywords\":\"Search query:\\n- PowerPoint title: website optimization\\n- Slide title: bullet point\\n- Image keywords: website design, user experience, load speed, SEO techniques\",\"url\":\"ppt-files-dev/6620bccd3c0565a9742c4c7a/image_1749548328408_ulbb6ovlki.png\",\"croppedWidth\":4.153333333333333,\"croppedheight\":4.153333333333333,\"isDelete\":false}},\"rawData\":{\"toc\":\"bullet point\",\"points\":[{\"title\":\"Page Speed\",\"description\":\"Optimize images and minify CSS for faster loading.\"},{\"title\":\"Mobile Friendly\",\"description\":\"Use responsive design to improve mobile user experience.\"},{\"title\":\"SEO Practices\",\"description\":\"Implement proper keywords and meta tags for better rankings.\"},{\"title\":\"Content Quality\",\"description\":\"Create relevant and engaging content to boost user retention.\"}]},\"staticData\":{\"number1\":\"01\",\"number2\":\"02\",\"number3\":\"03\",\"number4\":\"04\"}}",
    #                     "type": "AUTO_SHAPE",
    #                     "width": 12192000,
    #                     "x": 0,
    #                     "y": 0
    #                 }
    #             ],
    #             "slide_number": 2
    #         }
    #     ]
    # }

    # # Create presentation
    # prs = Presentation()
    # prs.slide_width = Inches(13.33)
    # prs.slide_height = Inches(7.5)


    # # Add shapes
    # for shape in json_data["slides"][0]["shapes"]:
    #     x = Emu(shape["x"])
    #     y = Emu(shape["y"])
    #     width = Emu(shape["width"])
    #     height = Emu(shape["height"])
        
    #     # Add auto shape if specified
    #     if shape["type"] == "AUTO_SHAPE":
    #         try:
    #             auto_shape_type = MSO_AUTO_SHAPE_TYPE[shape["auto_shape_type"]]
    #         except KeyError:
    #             auto_shape_type = MSO_AUTO_SHAPE_TYPE.RECTANGLE  # fallback

    #         shp = slide.shapes.add_shape(auto_shape_type, x, y, width, height)

    #         # Add text if present
    #         if shape.get("text"):
    #             shp.text = shape["text"]
    #             run = shp.text_frame.paragraphs[0].runs[0] if shp.text_frame.paragraphs[0].runs else shp.text_frame.paragraphs[0].add_run()
    #             run.text = shape["text"]

    #             if shape.get("font_size"):
    #                 run.font.size = Pt(shape["font_size"])
    #             if shape.get("bold") is not None:
    #                 run.font.bold = shape["bold"]
    #             if shape.get("italic") is not None:
    #                 run.font.italic = shape["italic"]
    #             if shape.get("color"):
    #                 try:
    #                     run.font.color.rgb = RGBColor.from_string(shape["color"])
    #                 except:
    #                     pass  # invalid color

    # # Save presentation
    # prs.save("recreated_slide.pptx")
