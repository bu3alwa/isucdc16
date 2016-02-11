[HttpPost]  
public ActionResult Index(HttpPostedFileBase file)  
{  
    size = 1024 * 2; //1024 bytes

    if (file != null && file.ContentLength > 0 && file.ContentLength < size )  
    {
        if(file.ContentType == "text")
        {
            try 
            {  
                string path = Path.Combine(Server.MapPath("~/"),Path.GetFileName(file.FileName));  
                file.SaveAs(path);  
                ViewBag.Message = "File uploaded successfully";  
            }  
            catch (Exception ex)  
            {  
                ViewBag.Message = "ERROR:" + ex.Message.ToString();  
            }  
        }
        else 
        {
            ViewBag.Message = "Not a text file.";
        }
    }
    else 
    {  
        ViewBag.Message = "You have not specified a file. Or size is too big";  
    }  
    return View();  
}
