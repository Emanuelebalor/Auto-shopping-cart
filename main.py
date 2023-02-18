from Items import Item

if __name__ == '__main__':
    with open("Test", 'r+') as file:
        file.truncate(0)

    item1 = Item()
    item1.loging_page_open().loging_page_credentials().get_all_items()\
        .add_item_to_cart("Apple iPhone 12, 128GB, Black", "Huawei Mate 20 Lite, 64GB, Black",
                          "Samsung Galaxy A32, 128GB, White", "Apple iPhone 13, 128GB, Blue", "Nokia 105, Black")\
        .change_item_quantity(3, 4, 5, 6, 7).remove_item_from_cart(2, 3).get_total_price().check_out_click()\
        .check_out_form_filler(1234567899, "Treppe zum Himmel", "Tromso").country_drop_down("Angola").submit_btn_clk()\
        .final_message()
