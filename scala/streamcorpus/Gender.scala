/**
 * generated by Scrooge ${project.version}
 */
package streamcorpus

import com.twitter.scrooge.ThriftEnum


@javax.annotation.Generated(value = Array("com.twitter.scrooge.Compiler"), date = "2013-08-12T15:12:53.355-0400")
case object Gender {
  
  case object Female extends Gender {
    val value = 0
    val name = "Female"
  }
  
  case object Male extends Gender {
    val value = 1
    val name = "Male"
  }

  /**
   * Find the enum by its integer value, as defined in the Thrift IDL.
   * @throws NoSuchElementException if the value is not found.
   */
  def apply(value: Int): Gender = {
    value match {
      case 0 => Female
      case 1 => Male
      case _ => throw new NoSuchElementException(value.toString)
    }
  }

  /**
   * Find the enum by its integer value, as defined in the Thrift IDL.
   * Returns None if the value is not found
   */
  def get(value: Int): Option[Gender] = {
    value match {
      case 0 => scala.Some(Female)
      case 1 => scala.Some(Male)
      case _ => scala.None
    }
  }

  def valueOf(name: String): Option[Gender] = {
    name.toLowerCase match {
      case "female" => scala.Some(Gender.Female)
      case "male" => scala.Some(Gender.Male)
      case _ => scala.None
    }
  }

  lazy val list: List[Gender] = scala.List[Gender](
    Female,
    Male
  )
}



@javax.annotation.Generated(value = Array("com.twitter.scrooge.Compiler"), date = "2013-08-12T15:12:53.355-0400")
sealed trait Gender extends ThriftEnum with Serializable