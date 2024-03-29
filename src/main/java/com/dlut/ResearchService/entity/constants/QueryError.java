package com.dlut.ResearchService.entity.constants;

/**
 * 查询反馈反馈
 */
public class QueryError {
    public static final String EXPRESSION_ERROR = "Check your query to make sure a valid expression are entered";
    public static final String BOOLEAN_OPERATORS_ERROR =
            "Check your query to make sure Boolean operators (AND, OR, NOT) are used properly.";
    public static final String QUERY_NOTIFICATION =
            "Please use parentheses to indicate set operations and try to avoid arbitrary usage." +
                    " Also, please do not enclose the entire expression in parentheses.";
}
