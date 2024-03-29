/*
 * 登录控制器，整个控制器不在校验登录拦截器的拦截范围内，控制器接口方法限制1s内最多访问2次。
 * 登录页面展示通知信息与登录栏。
 * 两种登录方式：邮箱验证码登录与账号密码登录。
 * 账号密码登录，输入账号密码后弹出验证码弹窗，输入验证码后校验登录。
 * 邮箱验证码登录，输入邮箱后，获取邮箱验证码，输入验证码后校验登录。
 * 第一次登录的用户采用邮箱登录后，会自动注册，注册结束后弹出设置账号密码弹窗。
 */
package com.dlut.ResearchService.controller.userController;

import com.dlut.ResearchService.annotation.RequestRateLimit;
import com.dlut.ResearchService.annotation.log;
import com.dlut.ResearchService.component.ResultBuilder;
import com.dlut.ResearchService.entity.constants.Result;
import com.dlut.ResearchService.service.impl.EmailCodeServiceImpl;
import com.dlut.ResearchService.service.impl.LoginServiceImpl;
import com.dlut.ResearchService.entity.constants.StatusCode;
import jakarta.annotation.Resource;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import org.jetbrains.annotations.NotNull;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RequestRateLimit
@RestController
@RequestMapping("login")
@CrossOrigin(origins = "http://localhost:3000")
public class LoginController {
    @Resource
    private EmailCodeServiceImpl emailCodeService;
    @Resource
    private LoginServiceImpl loginService;
    @Resource
    private ResultBuilder resultBuilder;

    @log
    @RequestMapping
    public void login(@NotNull HttpServletResponse response, @NotNull HttpSession session) throws IOException {
        try {
            loginService.login(response, session);
        }catch (Exception e){
            throw new IOException(e.getMessage());
        }
    }

    /**
     * 使用账号密码登录时获取验证码进行验证码校验，验证码刷新限制1s内最多1次，管理员登录需要校验管理员身份。
     * @param response 响应
     * @param session 会话
     * @throws IOException 读写异常
     */
    @log
    @GetMapping("sign-in/getCaptcha")
    public void getCaptcha(HttpServletResponse response, HttpSession session
                                ) throws IOException {
        emailCodeService.getCaptcha(response, session);
    }

    /**
     * 管理员模式
     * @param session
     * @param username
     * @param password
     * @param isManager
     * @return
     */
    @log
    @PostMapping("sign-in/manager")
    public Result signByManager(@NotNull HttpSession session,
                              @RequestParam String username,
                              @RequestParam String password,
                              @RequestParam String isManager){
        return loginService.signByAccount(session, username, password, isManager);
    }

    /**
     * 登陆，使用账号密码。
     * @param session 会话
     * @param username 邮箱或账号
     * @param password 密码
     * @param captcha 图片验证码
     */
    @log
    @PostMapping("sign-in/account")
    public Result signByAccount(
            @NotNull HttpSession session,
                                @RequestParam String username,
                                @RequestParam String password, @NotNull @RequestParam String captcha) {
        emailCodeService.checkCaptcha(session, captcha);
        return loginService.signByAccount(session, username, password);
    }

    /**
     * 登陆，验证码登陆。
     * @param email 邮箱
     * @param emailCode 邮箱验证码
     */
    @PostMapping("sign-in/emailCode")
    public Result signByEmailCode(@NotNull HttpSession session,
                                  @RequestParam String email,
                                  @RequestParam String emailCode){
        return loginService.signByEmailCodeOrRegistration(session, email, emailCode);
    }

    /**
     * 用户注册
     * @param email 注册邮箱
     * @param emailCode 邮箱验证码
     */
    @PostMapping("sign-up/registration")
    public Result registration(@NotNull HttpSession session,
                               @RequestParam String email,
                               @RequestParam String emailCode){
        return loginService.signByEmailCodeOrRegistration(session, email, emailCode);
    }

    /**
     * 设置密码，密码设置成功后修改或导入数据库
     * @param password 密码
     */
    @PostMapping("setAccountAndPassword")
    public Result setPassword(@NotNull HttpSession session,
                              @RequestParam String password,
                              @RequestParam Integer account){
        return loginService.setPassword(session, account, password);
    }

    /**
     * 发送邮件验证码
     * @param email 目标邮箱
     */
    @PostMapping("sendEmailCode")
    public Result sendEmailCode(String email){
        emailCodeService.sendEmailCode(email);
        return resultBuilder.build(StatusCode.STATUS_CODE_200,"验证码已发送", null);
    }

    @PostMapping("recoveryPassword")
    public Result recoveryPassword(HttpSession session, String email, String emailCode){
        return loginService.recoveryPassword(session, email, emailCode);
    }
}
