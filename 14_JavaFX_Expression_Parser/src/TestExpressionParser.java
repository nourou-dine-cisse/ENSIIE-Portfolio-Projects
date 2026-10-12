import expressions.Expression;
import java.util.List;
import parser.ExpressionParser;

public class TestExpressionParser {
    public static void main(String[] args) {
        try {
            ExpressionParser<Integer> parser = new ExpressionParser<>(0);

            // Test 1 : Affectation simple
            List<Expression<Integer>> exprs1 = parser.parse("c=1+2");
            Expression<Integer> expr1 = exprs1.get(0);
            System.out.println("Test 1 : c=1+2");
            System.out.println("hasValue: " + expr1.hasValue());
            System.out.println("value: " + expr1.value());

            // Test 2 : Affectation avec parenthèses
            List<Expression<Integer>> exprs2 = parser.parse("d=(2+3)");
            Expression<Integer> expr2 = exprs2.get(0);
            System.out.println("\nTest 2 : d=(2+3)");
            System.out.println("hasValue: " + expr2.hasValue());
            System.out.println("value: " + expr2.value());

            // Test 3 : Affectations en chaîne
            parser.parse("a=2; b=3; c=a+b");
            List<Expression<Integer>> exprs3 = parser.parse("c");
            Expression<Integer> expr3 = exprs3.get(0);
            System.out.println("\nTest 3 : a=2; b=3; c=a+b puis c");
            System.out.println("hasValue: " + expr3.hasValue());
            System.out.println("value: " + expr3.value());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}