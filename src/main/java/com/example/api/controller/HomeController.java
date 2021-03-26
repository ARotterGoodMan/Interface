package com.example.api.controller;

import com.alibaba.fastjson.JSONObject;
import com.example.api.entity.home.*;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 邵潇遥
 * @Classname com.example.api.controller.HoneController
 * @Description TODO
 * @Date 2020/11/10 19:22
 * @Created by 邵潇遥
 * <p>
 * 类里面分别有get，post，dealWith三个方法。
 * get方法用于接收客户端的GET请求，post方法用于接收客户端的POST请求，
 * dealWith方法用于处理客户端传输来数据并返回处理的结果。
 * <p>
 * get方法会自动把客户端传来的表单的数据解析出来再保存到info变量中，
 * 该方法的返回值是一个对象时，会默认将对象转换为Json格式返回。
 * post方法的传入形参和返回的值的流程差不多，不同的是，
 * POST请求时把请求体的数据解析出来再保存到info变量中，
 * 而且请求体的数据格式必须为Json格式。
 */
@RestController
@RequestMapping(value = "/home")
public class HomeController {

    @GetMapping(value = "/multidata")
    public Object get(SetHomeData1 setHomeData1) {
        return firstDealWith(setHomeData1);

    }

    @PostMapping(value = "/multidata")
    public Object post(SetHomeData1 setHomeData1) {
        return firstDealWith(setHomeData1);
    }

    @GetMapping(value = "/data")
    public Object gets(Afferent afferent) {
        return nextDealWith(afferent);
    }

    @PostMapping(value = "/data")
    public Object posts(Afferent afferent) {
        return nextDealWith(afferent);

    }

    private Object firstDealWith(SetHomeData1 setHomeData1) {
        ShowHomeData1 showHomeData1 = new ShowHomeData1();
        setHomeData1.setBanner(showHomeData1.setBannerlist());
        setHomeData1.setdKeyword(showHomeData1.setdKeywordlist());
        setHomeData1.setKeywords(showHomeData1.setKeywordslist());
        setHomeData1.setRecommend(showHomeData1.setRecommendlist());
        return setHomeData1.read();
    }

    public Object nextDealWith(Afferent afferent) {
        JSONObject json = new JSONObject();
        if (afferent.getType() == null && afferent.getPage() == 0) {
            json.put("错误信息", "未传该有的属性 type 和 page");
        } else if (afferent.getType() == null) {
            json.put("错误信息", "未传该有的属性 type");
        } else if (afferent.getPage() == 0) {
            json.put("错误信息", "未传该有的属性 page 或 page等于0");
        } else {
            String type = afferent.getType();
            int page = afferent.getPage();
            SetHomeData2 setHomeData2 = new SetHomeData2();
            setHomeData2.setTypePage(type,page);
            setHomeData2.setData();
            ShowHomeData2 showHomeData2 = new ShowHomeData2();
            showHomeData2.setData(setHomeData2.getData());
            return showHomeData2.getData();
        }
        return json;
    }

}
