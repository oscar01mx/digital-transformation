package gcfv2;

import java.io.BufferedWriter;

import com.google.cloud.functions.HttpFunction;
import com.google.cloud.functions.HttpRequest;
import com.google.cloud.functions.HttpResponse;

public class HelloHttpFunction implements HttpFunction {
  public void service(final HttpRequest request, final HttpResponse response) throws Exception {
    final String name = request.getQuery().get();
    final BufferedWriter writer = response.getWriter();
    writer.write("Hello " + name + "!");
  }
}
