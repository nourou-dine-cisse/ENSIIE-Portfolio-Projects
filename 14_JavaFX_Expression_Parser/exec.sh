/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home/bin/javac \
--module-path /Users/nouroudine/Documents/javafx-sdk-24.0.1/lib \
--add-modules javafx.controls,javafx.fxml \
-d bin $(find src -name "*.java" | grep -v tests)
/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home/bin/java \
--module-path /Users/nouroudine/Documents/javafx-sdk-24.0.1/lib \
--add-modules javafx.controls,javafx.fxml \
-cp bin application.MainFX
