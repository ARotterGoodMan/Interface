package com.example.api.entity.home;

import com.alibaba.fastjson.JSONObject;
import com.example.api.entity.home.homedata2.popdatas.*;

import java.util.LinkedHashMap;
import java.util.Objects;

public class SetHomeData2 {
    private String type;
    private int page;
    private JSONObject data = new JSONObject(new LinkedHashMap());

    public void setTypePage(String type, int page) {
        this.type = type;
        this.page = page;
    }

    public void setData() {
        if (getType().equals("pop")) {
            switch (getPage()) {
                case 1:
                    DataPage1 dataPage1 = new DataPage1();
                    dataPage1.setDatas();
                    this.data = dataPage1.getDatas();
                    break;
                case 2:
                    DataPage2 dataPage2= new DataPage2();
                    dataPage2.setDatas();
                    this.data = dataPage2.getDatas();
                    break;
                case 3:
                    DataPage3 dataPage3 = new DataPage3();
                    dataPage3.setDatas();
                    this.data = dataPage3.getDatas();
                    break;
                case 4:
                    DataPage4 dataPage4 = new DataPage4();
                    dataPage4.setDatas();
                    this.data = dataPage4.getDatas();
                    break;
                default:
                    DataPage5 dataPageOther = new DataPage5();
                    dataPageOther.setPage(getPage());
                    dataPageOther.setDatas();
                    this.data = dataPageOther.getDatas();
                    break;
            }
        }

    }

    public String getType() {
        return type;
    }

    public int getPage() {
        return page;
    }

    public JSONObject getData() {
        return data;
    }
}
