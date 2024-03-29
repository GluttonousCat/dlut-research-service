-- ----------------------------
-- 日志表
-- ----------------------------
drop table if exists sys_ops_log;
create table sys_ops_log (
        ops_id            bigint(20)      not null auto_increment    comment '日志主键',
        title             varchar(50)     default ''                 comment '模块标题',
        business_type     int(2)          default 0                  comment '业务类型（0其它 1新增 2修改 3删除）',
        method            varchar(100)    default ''                 comment '方法名称',
        request_method    varchar(10)     default ''                 comment '请求方式',
        operator_type     int(1)          default 0                  comment '操作类别（0其它 1后台用户 2普通用户）',
        ops_name          varchar(50)     default ''                 comment '操作人员',
        dept_name         varchar(50)     default ''                 comment '部门名称',
        ops_url           varchar(255)    default ''                 comment '请求URL',
        ops_ip            varchar(128)    default ''                 comment '主机地址',
        ops_location      varchar(255)    default ''                 comment '操作地点',
        ops_param         varchar(2000)   default ''                 comment '请求参数',
        json_result       varchar(2000)   default ''                 comment '返回参数',
        status            int(1)          default 0                  comment '操作状态（0正常 1异常）',
        error_msg         varchar(2000)   default ''                 comment '错误消息',
        ops_time          datetime                                   comment '操作时间',
        cost_time         bigint(20)      default 0                  comment '消耗时间',
        primary key (ops_id),
        key idx_sys_ops_log_bt (business_type),
        key idx_sys_ops_log_s  (status),
        key idx_sys_ops_log_ot (ops_time)
) engine=innodb auto_increment=100 comment = '操作日志记录';

-- ----------------------------
-- 访问日志表
-- ----------------------------
drop table if exists sys_ops_log;
create table sys_ops_log (
    ops_id            bigint(20)      not null auto_increment    comment '日志主键',
    method            varchar(100)    default ''                 comment '方法名称',
    request_method    varchar(10)     default ''                 comment '请求方式',
    operator_type     int(1)          default 0                  comment '操作类别（0其它 1后台用户 2普通用户）',
    ops_name          varchar(50)     default ''                 comment '操作人员',
    ops_url           varchar(255)    default ''                 comment '请求URL',
    ops_ip            varchar(128)    default ''                 comment '主机地址',
    ops_param         varchar(2000)   default ''                 comment '请求参数',
    json_result       varchar(2000)   default ''                 comment '返回参数',
    status            int(1)          default 0                  comment '操作状态（0正常 1异常）',
    error_msg         varchar(2000)   default ''                 comment '错误消息',
    ops_time          datetime                                   comment '操作时间',
    cost_time         bigint(20)      default 0                  comment '消耗时间',
    primary key (ops_id),
    key idx_sys_ops_log_s  (status),
    key idx_sys_ops_log_ot (ops_time)
) engine=innodb auto_increment=100 comment = '接口访问日志';

-- ----------------------------
-- 用户表
-- ----------------------------
drop table if exists sys_user;
create table sys_user (
        user_id           bigint(20)      not null auto_increment    comment '用户主键',
        nack_name         varchar(20)     default null               comment '用户昵称',
        account           bigint(20)      default null               comment '用户账号',
        email             varchar(50)     default ''                 comment '用户邮箱',
        password          varchar(50)     default null               comment '用户密码',
        salt              varchar(20)     default ''                 comment '盐加密',
        avatar            varchar(100)    default null               comment '头像路径',
        sex               char(1)         default '0'                comment '性别(0未知1男2女)',
        user_type         varchar(2)      default '00'               comment '用户类型(00系统用户01注册用户)',
        status            tinyint(1)      default 0                  comment '账号状态（0正常 1停用）',
        registration_time datetime                                   comment '创建时间',
        last_login_time   datetime                                   comment '最后登陆时间',
        login_ip          varchar(128)    default ''                 comment '最后登陆IP',
        last_update_time  datetime                                   comment '上次修改时间',
        remark            varchar(500)    default null               comment '备注内容',
        primary key (user_id),
        key idx_user_account (account),
        key idx_user_email   (email)
) engine=innodb auto_increment=0 comment = '用户表';

-- ----------------------------
-- 文献表
-- ----------------------------
-- 删除外键约束
ALTER TABLE abstract DROP FOREIGN KEY fk_abstract_paper;

drop table if exists paper;
create table paper (
    paper_id       bigint(20)        not null auto_increment    comment '文献id',
    tl             varchar(500)      default null               comment 'TL文章标题',
    au             TEXT              default null               comment 'AU文章作者',
    de             TEXT              default null               comment 'DE关键词',
    so             varchar(500)      default null               comment 'SO文章期刊',
    py             varchar(4)        default null               comment 'PY发表年份',
    wc             varchar(500)      default null               comment 'WOS分类',
    esi            varchar(100)      default null               comment 'ESI分类',
    tc             smallint(5)       default 0                  comment '文章被引量',
    nr             smallint(5)       default 0                  comment '文章引文量',
    ab             varchar(1500)     default null               comment '文献摘要（1500字符）',
    ab_id          bigint(20)        not null                   comment '摘要id',
    doi            varchar(500)      default null               comment '论文DOI号',
    cr             text              default null               comment '引文DOI',
    primary key (paper_id),
    UNIQUE INDEX idx_paper_tl (tl),
    UNIQUE INDEX idx_paper_ab (ab_id),
    KEY idx_paper_doi (doi)
) engine=innodb auto_increment=0 comment = '文献表';

-- ----------------------------
-- 摘要表
-- ----------------------------
drop table if exists abstract;
create table abstract (
                          abstract_id          bigint(20)       not null auto_increment    comment '机构id',
                          paper_id             bigint(20)       not null                   comment '论文id',
                          paper_doi            varchar(50)      default null               comment '论文DOI',
                          abstract             text             default null               comment '摘要全文',
                          research_background  varchar(2000)    default null               comment '研究背景',
                          research_method      varchar(2000)    default null              comment '研究方法',
                          research_result      varchar(2000)    default null              comment '研究结果',
                          research_conclusion  varchar(2000)    default null              comment '研究结论',
                          primary key (abstract_id),
                          unique key idx_abstract_paper_id (paper_id),
                          key idx_abstract_paper_doi (paper_doi),
                          CONSTRAINT fk_abstract_paper FOREIGN KEY (paper_id) REFERENCES paper(paper_id)
                              ON DELETE CASCADE
                              ON UPDATE CASCADE
) engine=innodb auto_increment=0 comment = '摘要表';

-- ----------------------------
-- 作者表
-- ----------------------------
drop table if exists author;
create table author (
        author_id               bigint(20)      not null auto_increment    comment '作者id',
        author_name             varchar(200)    not null                   comment '作者姓名',
        author_country          varchar(100)    default null               comment '作者国家',
        author_org              varchar(2000)   default null               comment '作者机构',
        paper_count             varchar(50)     default null               comment '发文数量',
        paper_count_per_year    varchar(4)      default null               comment '每年发文数量',
        # research                varchar(200)    default null               comment '研究领域',
        H                       smallint(4)     default 0                  comment 'H指数',
        high_cited_paper        smallint(4)     default 0                  comment '高被引文章',
        primary key (author_id),
        KEY idx_author_name (author_name),
        KEY idx_author_org (author_org)
) engine=innodb auto_increment=0 comment = '作者表';

-- ----------------------------
-- 关键词表
-- ----------------------------
drop table if exists keyword;
create table keyword (
    keyword_id     bigint(20)   not null auto_increment   comment '关键词id',
    keyword_name   varchar(50)  default null              comment '关键词名称',
    keyword_count  int(100)     default 1                 comment '关键词频次',
    research       varchar(200) default null              comment '研究领域',
    primary key (keyword_id),
    key idx_keyword_kn(keyword_name)
) engine=innodb auto_increment=0 comment = '关键词表';

-- ----------------------------
-- 机构表
-- ----------------------------
drop table if exists organization;
create table organization (
        org_id             bigint(20)      not null auto_increment    comment '机构id',
        org_name           varchar(200)    default null               comment '机构名称',
        org_country        varchar(100)    default null               comment '机构国家',
        org_paper_count    varchar(100)    default null               comment '机构发文数',
        org_author_count   varchar(50)     default null               comment '机构作者数',
        primary key (org_id)
) engine=innodb auto_increment=0 comment = '机构表';

-- ----------------------------
-- 通知表
-- ----------------------------
drop table if exists notice;
create table notice (
        notice_id        bigint(20)   not null auto_increment    comment '通知id',
        create_time      datetime     default null               comment '创建时间',
        create_by        varchar(5)   default null               comment '创建人',
        title            varchar(100) default null               comment '通知标题',
        content          varchar(500) default null               comment '通知内容',
        status           tinyint(1)   default 0                  comment '通知状态（0正常 1停用）',
        target_page      smallint(2)  default null               comment '通知页面（0登陆页面 1主页面 ）',
        primary key (notice_id)
) engine=innodb auto_increment=0 comment = '通知表';

-- ----------------------------
-- 字典数据表
-- ----------------------------
drop table if exists sys_dict_data;
create table sys_dict_data (
        dict_code    bigint(20)     not null auto_increment    comment '字典编码',
        dict_name    varchar(100)   default null               comment '字典名称',
        dict_sort    varchar(100)   default null               comment '字典排序',
        dict_label   varchar(100)   default null               comment '字典标签',
        dict_value   varchar(100)   default null               comment '字典键值',
        dict_type    varchar(100)   default null               comment '字典类型',
        status       char(1)        default null               comment '状态（0正常，1停用）',
        create_by    varchar(50)    default null               comment '创建者',
        create_time  varchar(4)     default null               comment '创建时间',
        update_by    varchar(100)   default null               comment '更新者',
        update_time  varchar(50)    default null               comment '更新类型',
        remark       smallint(5)    default 0                  comment '备注',
        primary key (dict_code)
) engine=innodb auto_increment=0 comment = '字典数据表';
#
# -- ----------------------------
# -- 3、作者表
# -- ----------------------------
# drop table if exists sys_author;
# create table sys_author (
#     author_id         bigint(20)      not null auto_increment    comment '作者id',
#     author_name       varchar(200)    default null               comment 'TL标题',
#     author_country    varchar(100)    default null comment 'AU作者',
#     author_org        varchar(100)    default null comment 'DE关键词',
#     so             varchar(50)        default null comment 'SO期刊',
#     py             varchar(4)   default null comment 'PY发表年份',
#     wc             varchar(100) default null comment 'WOS分类',
#     esi            varchar(50)  default null comment 'ESI分类',
#     tc             smallint(5)  default 0 comment '被引量',
#     nc             smallint(5)  default 0 comment '引文量',
#     ab             TEXT         default null comment '文献摘要',
#     primary key (author_id)
# ) engine=innodb auto_increment=0 comment = '作者表';

